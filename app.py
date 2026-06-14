from flask import Flask, render_template, request, redirect, session, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from db_config import get_connection
import requests

app = Flask(__name__)
app.secret_key = "maritime_secret_key"


def calculate_voyage(distance, speed):
    days = distance / (speed * 24)
    fuel_used = days * 32
    fuel_cost = fuel_used * 463
    total_cost = fuel_cost + 45000 + 120000

    return {
        "days": round(days, 2),
        "fuel_used": round(fuel_used, 2),
        "fuel_cost": round(fuel_cost, 2),
        "total_cost": round(total_cost, 2),
        "weather_risk": "High",
        "gale_risk": "18% - 22%",
        "sea_state": "BF 7",
        "diversion": "8° Southward Deviation Recommended"
    }


@app.route("/")
def home():
    return render_template("index.html")


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
            return redirect("/dashboard")

        return render_template("login.html", error="Invalid username or password")

    except Exception as e:
        return render_template(
            "login.html",
            error=str(e)
        )


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/login-page")


@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/login-page")

    return render_template(
        "dashboard.html",
        total_cost=801127,
        detour_saving=9200,
        distance=8412,
        detour_distance=312,
        voyage_days=29.2,
        extra_days=1.1,
        eca_distance=2353,
        non_eca_distance=6059,
        max_bf_main="BF 7",
        max_bf_detour="BF 3",
        gale_main="18-22%",
        gale_detour="2.1%",
        total_bunker=934,
        total_fuel=432227
    )


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
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vessel ORDER BY vessel_id DESC")
        vessels = cursor.fetchall()
        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)
        vessels = []

    return render_template("vessel.html", vessels=vessels)


@app.route("/add-vessel", methods=["POST"])
def add_vessel():
    vessel_name = request.form["vessel_name"]
    dwt = request.form["dwt"]
    draft = request.form["draft"]
    speed = request.form["speed"]

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO vessel
            (vessel_name, dwt, draft, speed)
            VALUES (%s,%s,%s,%s)
            """,
            (vessel_name, dwt, draft, speed)
        )

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)

    return redirect("/vessel")


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

        cursor.execute("SELECT IFNULL(SUM(total_cost), 0) FROM voyage")
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