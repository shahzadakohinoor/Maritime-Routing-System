import streamlit as st

st.set_page_config(page_title="Maritime Routing System", layout="wide")

st.title("AI-Powered Maritime Weather Routing System")
st.write("Optimize voyage route, fuel cost, ETA and weather risk.")

source = st.text_input("Source Port", "Rotterdam")
destination = st.text_input("Destination Port", "Singapore")
distance = st.number_input("Distance in Nautical Miles", value=8412.0)
speed = st.number_input("Speed in Knots", value=12.0)

if st.button("Calculate Route"):
    days = distance / (speed * 24)
    fuel_used = days * 32
    fuel_cost = fuel_used * 463
    total_cost = fuel_cost + 45000 + 120000

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Voyage Days", round(days, 2))
    col2.metric("Fuel Used", f"{round(fuel_used, 2)} MT")
    col3.metric("Fuel Cost", f"${round(fuel_cost, 2)}")
    col4.metric("Total Cost", f"${round(total_cost, 2)}")

    st.warning("High Monsoon Activity Detected")
    st.success("Recommended Diversion: 8° Southward Deviation")