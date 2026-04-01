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
