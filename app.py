import streamlit as st
import random

st.set_page_config(page_title="Smart Irrigation System", layout="wide")

# -------------- SIMULATED SENSOR DATA ----------------
def get_sensor_data():
    soil = random.randint(20, 90)
    temp = random.randint(22, 38)
    hum = random.randint(30, 80)
    pump = "ON" if soil < 40 else "OFF"
    return soil, temp, hum, pump

# -------------- CHATBOT FUNCTION ----------------
def irrigation_chatbot(user_message):
    user_message = user_message.lower()

    if "when to water" in user_message:
        return "Water when soil moisture goes below 40%."

    if "disease" in user_message:
        return "Your crop may have fungal infection if leaves are yellow. Apply suitable fungicide."

    if "irrigation" in user_message:
        return "Irrigation depends on soil moisture and temperature. Keep soil between 40–60% moisture."

    return "I am not sure about this. Try asking about irrigation, watering time, or crop disease."

# ------------------- UI LAYOUT -------------------
st.title("🌱 Smart Irrigation Dashboard + Chatbot")

col1, col2 = st.columns(2)

# ------- Dashboard Section -------
with col1:
    st.subheader("📊 Live Sensor Dashboard")

    soil, temp, hum, pump = get_sensor_data()

    st.metric("Soil Moisture (%)", soil)
    st.metric("Temperature (°C)", temp)
    st.metric("Humidity (%)", hum)
    st.metric("Pump Status", pump)

# ------- Chatbot Section -------
with col2:
    st.subheader("🤖 Smart Farming Chatbot")

    user_input = st.text_input("Ask something about farming / irrigation:")

    if st.button("Ask"):
        reply = irrigation_chatbot(user_input)
        st.success(reply)