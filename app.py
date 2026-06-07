from flask import Flask, render_template, request, send_file, redirect, session, url_for
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from db_config import get_connection
import requests
import os

app = Flask(__name__)
app.secret_key = "maritime_secret_key"


def calculate_voyage(distance, speed):
    days = distance / (speed * 24)

    fuel_per_day = 32
    fuel_price = 463
    port_charges = 45000
    canal_charges = 120000

    fuel_used = days * fuel_per_day
    fuel_cost = fuel_used * fuel_price
    total_cost = fuel_cost + port_charges + canal_charges

    return {
        "days": round(days, 2),
        "fuel_used": round(fuel_used, 2),
        "fuel_cost": round(fuel_cost, 2),
        "total_cost": round(total_cost, 2),
        "port_charges": port_charges,
        "canal_charges": canal_charges,
        "gale_risk": "18% - 22%",
        "sea_state": "BF 7",
        "diversion": "8° Southward Deviation Recommended",
        "weather_risk": "High"
    }


def get_marine_weather():
    try:
        url = "https://marine-api.open-meteo.com/v1/marine"

        params = {
            "latitude": 12,
            "longitude": 65,
            "hourly": "wave_height,wave_direction,wave_period",
            "timezone": "auto"
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        wave_height = data["hourly"]["wave_height"][0]
        wave_direction = data["hourly"]["wave_direction"][0]
        wave_period = data["hourly"]["wave_period"][0]

    except Exception as e:
        print("Weather API Error:", e)
        wave_height = 4.2
        wave_direction = 240
        wave_period = 8

    if wave_height >= 4:
        risk_level = "High"
    elif wave_height >= 2:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return wave_height, wave_direction, wave_period, risk_level


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/route", methods=["POST"])
def route():
    source = request.form["source"]
    destination = request.form["destination"]
    distance = float(request.form["distance"])
    speed = float(request.form["speed"])

    result = calculate_voyage(distance, speed)

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO voyage
        (source_port, destination_port, distance_nm, speed,
        voyage_days, fuel_used, fuel_cost, total_cost,
        weather_risk, diversion_suggestion)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            source,
            destination,
            distance,
            speed,
            result["days"],
            result["fuel_used"],
            result["fuel_cost"],
            result["total_cost"],
            result["weather_risk"],
            result["diversion"]
        )

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)

    return render_template(
        "route.html",
        source=source,
        destination=destination,
        distance=distance,
        speed=speed,
        days=result["days"],
        fuel_used=result["fuel_used"],
        fuel_cost=result["fuel_cost"],
        total_cost=result["total_cost"],
        gale_risk=result["gale_risk"],
        sea_state=result["sea_state"],
        diversion=result["diversion"]
    )


@app.route("/weather")
def weather():
    wave_height, wave_direction, wave_period, risk_level = get_marine_weather()

    return render_template(
        "weather.html",
        wave_height=wave_height,
        wave_direction=wave_direction,
        wave_period=wave_period,
        risk_level=risk_level
    )


@app.route("/history")
def history():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM voyage ORDER BY voyage_id DESC")
        voyages = cursor.fetchall()

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)
        voyages = []

    return render_template("history.html", voyages=voyages)


@app.route("/vessel")
def vessel():
    return render_template("vessel.html")


@app.route("/add-vessel", methods=["POST"])
def add_vessel():
    vessel_name = request.form["vessel_name"]
    dwt = request.form["dwt"]
    draft = request.form["draft"]
    speed = request.form["speed"]

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO vessel
        (vessel_name, dwt, draft, speed)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(sql, (vessel_name, dwt, draft, speed))
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)

    return redirect("/vessel")


@app.route("/login-page")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session["admin"] = username
            return redirect("/admin")

        return render_template("login.html", error="Invalid username or password")

    except Exception as e:
        print("Database Error:", e)
        return render_template("login.html", error="Database connection failed")


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")


@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/login-page")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM voyage")
        total_voyages = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM vessel")
        total_vessels = cursor.fetchone()[0]

        cursor.execute("SELECT IFNULL(SUM(total_cost),0) FROM voyage")
        total_cost = cursor.fetchone()[0]

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)
        total_voyages = 0
        total_vessels = 0
        total_cost = 0

    return render_template(
        "admin.html",
        total_voyages=total_voyages,
        total_vessels=total_vessels,
        total_cost=round(total_cost, 2)
    )


@app.route("/map")
def map_page():
    return render_template("map.html")


@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/download-report")
def download_report():
    filename = "voyage_report.pdf"

    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(80, 800, "Maritime Voyage Report")

    c.setFont("Helvetica", 12)
    c.drawString(80, 760, "Project: AI-Powered Maritime Weather Routing System")
    c.drawString(80, 730, "Route: Rotterdam to Singapore")
    c.drawString(80, 710, "Distance: 8412 NM")
    c.drawString(80, 690, "Speed: 12 Knots")
    c.drawString(80, 670, "Voyage Days: 29.21")
    c.drawString(80, 650, "Fuel Used: 934.67 MT")
    c.drawString(80, 630, "Fuel Cost: $432,750")
    c.drawString(80, 610, "Port Charges: $45,000")
    c.drawString(80, 590, "Canal Charges: $120,000")
    c.drawString(80, 570, "Total Cost: $597,750")
    c.drawString(80, 540, "Weather Risk: High")
    c.drawString(80, 520, "Gale Risk: 18% - 22%")
    c.drawString(80, 500, "Sea State: BF 7")
    c.drawString(80, 480, "Recommended Diversion: 8 Degrees Southward Deviation")

    c.save()

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)