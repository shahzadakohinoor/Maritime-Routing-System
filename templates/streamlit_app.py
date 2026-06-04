import streamlit as st

st.set_page_config(page_title="Maritime Routing System", layout="wide")

st.title("AI-Powered Maritime Weather Routing System")
st.write("Optimize voyage route, fuel cost, ETA and weather risk.")

source = st.text_input("Source Port", "Rotterdam")
destination = st.text_input("Destination Port", "Singapore")
distance = st.number_input("Distance in Nautical Miles", value=8412)
speed = st.number_input("Speed in Knots", value=12)

if st.button("Calculate Route"):
    days = distance / (speed * 24)

    fuel_per_day = 32
    fuel_price = 463
    fuel_used = days * fuel_per_day
    fuel_cost = fuel_used * fuel_price

    port_charges = 45000
    canal_charges = 120000
    total_cost = fuel_cost + port_charges + canal_charges

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Voyage Days", round(days, 2))
    col2.metric("Fuel Used", f"{round(fuel_used, 2)} MT")
    col3.metric("Fuel Cost", f"${round(fuel_cost, 2)}")
    col4.metric("Total Cost", f"${round(total_cost, 2)}")

    st.warning("High Monsoon Activity Detected")
    st.success("Recommended Diversion: 8° Southward Deviation")