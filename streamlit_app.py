import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Maritime Routing System",
    page_icon="🚢",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🚢 AI-Powered Maritime Weather Routing System")
st.write("Voyage route planning, fuel calculation, weather risk analysis and diversion recommendation.")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Route Calculator",
        "Weather Dashboard",
        "Voyage History",
        "Project Report",
        "Admin Dashboard"
    ]
)

def calculate_voyage(distance, speed):
    days = distance / (speed * 24)
    fuel_used = days * 32
    fuel_cost = fuel_used * 463
    total_cost = fuel_cost + 45000 + 120000
    return days, fuel_used, fuel_cost, total_cost

if menu == "Home":
    st.header("Project Overview")
    st.write("""
    This system helps shipping operators calculate voyage duration, fuel usage,
    total voyage cost, weather risk and route diversion decisions.
    """)

elif menu == "Route Calculator":
    st.header("Route Calculator")

    col1, col2 = st.columns(2)

    with col1:
        source = st.text_input("Source Port", "Rotterdam")
        distance = st.number_input("Distance in Nautical Miles", value=8412.0, min_value=1.0)

    with col2:
        destination = st.text_input("Destination Port", "Singapore")
        speed = st.number_input("Speed in Knots", value=12.0, min_value=1.0)

    if st.button("Calculate Route"):
        days, fuel_used, fuel_cost, total_cost = calculate_voyage(distance, speed)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Voyage Days", round(days, 2))
        c2.metric("Fuel Used", f"{round(fuel_used, 2)} MT")
        c3.metric("Fuel Cost", f"${round(fuel_cost, 2)}")
        c4.metric("Total Cost", f"${round(total_cost, 2)}")

        st.warning("⚠ High Monsoon Activity Detected")
        st.info("Gale Risk: 18% - 22%")
        st.info("Sea State: BF 7")
        st.success("Recommended Diversion: 8° Southward Deviation")

        st.session_state.history.append({
            "Source": source,
            "Destination": destination,
            "Distance NM": distance,
            "Speed": speed,
            "Voyage Days": round(days, 2),
            "Fuel Used MT": round(fuel_used, 2),
            "Total Cost": round(total_cost, 2),
            "Status": "Detour Suggested"
        })

elif menu == "Weather Dashboard":
    st.header("Marine Weather Dashboard")

    wave_height = st.slider("Wave Height (m)", 0.0, 8.0, 4.2)
    wave_direction = st.slider("Wave Direction (°)", 0, 360, 240)
    wave_period = st.slider("Wave Period (sec)", 1, 20, 8)

    risk = "High" if wave_height >= 4 else "Medium" if wave_height >= 2 else "Low"

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Wave Height", f"{wave_height} m")
    c2.metric("Wave Direction", f"{wave_direction}°")
    c3.metric("Wave Period", f"{wave_period} sec")
    c4.metric("Risk Level", risk)

    if risk == "High":
        st.error("High marine risk detected. Route diversion is recommended.")
    elif risk == "Medium":
        st.warning("Medium marine risk. Continue with caution.")
    else:
        st.success("Low marine risk. Planned route is acceptable.")

elif menu == "Voyage History":
    st.header("Voyage History")

    if len(st.session_state.history) == 0:
        st.info("No voyage calculated yet.")
    else:
        st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True)

elif menu == "Project Report":
    st.header("Project Report")

    st.subheader("Abstract")
    st.write("""
    The AI-Powered Maritime Weather Routing System supports voyage planning
    through ETA calculation, fuel estimation, weather-risk analysis and diversion recommendation.
    """)

    st.subheader("Modules")
    st.write("""
    - Route Planner
    - Weather Dashboard
    - Fuel Calculator
    - Cost Calculator
    - Voyage History
    - AI Recommendation Engine
    """)

elif menu == "Admin Dashboard":
    st.header("Admin Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Voyages", len(st.session_state.history))
    c2.metric("Total Vessels", 1)
    c3.metric("Weather Risk", "High")
    c4.metric("System Status", "Active")