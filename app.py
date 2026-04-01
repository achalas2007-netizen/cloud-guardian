import streamlit as st
import random

st.title("☁️ Cloud Guardian - HITL System")

# Mock data (later replaced by Harish's data)
data = {
    "service": "EC2",
    "cpu": random.randint(40, 100),
    "cost": random.randint(100, 500),
    "traffic": random.randint(200, 1500)
}

st.subheader("📊 Incoming Cloud Metrics")
st.write(data)
# Detection logic
anomaly = data["cpu"] > 85

if data["cpu"] > 85 and data["cost"] > 250:
    risk = "HIGH"
elif data["cpu"] > 70:
    risk = "MEDIUM"
else:
    risk = "LOW"

st.subheader("🔍 Analysis")
st.write(f"Anomaly Detected: {anomaly}")
st.write(f"Risk Level: {risk}")
if anomaly and risk == "HIGH":
    st.error("🚨 HIGH RISK DETECTED!")

    st.subheader("👨‍💻 Human Decision Panel")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve"):
            st.success("Action Approved")

    with col2:
        if st.button("❌ Ignore"):
            st.warning("Ignored by user")
            efficiency = data["traffic"] / data["cost"]

st.subheader("💡 Efficiency Analysis")
st.write(f"Efficiency Score: {efficiency:.2f}")

if efficiency < 3:
    st.warning("Low efficiency → Reduce service")
else:
    st.success("High efficiency → Protect service")
