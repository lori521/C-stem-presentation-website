import streamlit as st
import numpy as np
import time

# Setări pagină
st.set_page_config(page_title="C-Stem | Infrastructure AI", layout="centered")

# Header
st.title("🏗️ C-Stem")
st.subheader("The A.I. nervous system for infrastructure.")
st.write("We deploy advanced DSP sensors to capture the precise vibrational frequencies of any building. Our Physics-Informed AI detects invisible micro-cracks, then simulates exactly how and when a structure will fail to prevent sudden, deadly collapses.")

st.divider()

# Simulare de semnal (Zgomot vs Frecvență naturală)
st.write("### Live Sensor Data: Bridge Pillar 4")
t = np.linspace(0, 10, 100)
# Generăm un semnal fals cu puțin zgomot
signal = np.sin(t) + np.random.normal(0, 0.1, 100) 

# Afișăm graficul
st.line_chart(signal)

st.success("System Status: Monitoring structural integrity. No anomalies detected.")
