import streamlit as st
import numpy as np
import time

# Configurare pagină
st.set_page_config(page_title="C-Stem | Infrastructure AI", layout="centered")

# Inițializare memorie stare (pentru a ține minte dacă am declanșat fisura)
if 'fisura_activa' not in st.session_state:
    st.session_state.fisura_activa = False

# Header
st.title("🏗️ C-Stem")
st.markdown("**The A.I. nervous system for infrastructure.**")
st.write("We deploy advanced DSP sensors to capture the precise vibrational frequencies of any building. Our Physics-Informed AI detects invisible micro-cracks, then simulates exactly how and when a structure will fail to prevent sudden, deadly collapses.")

st.divider()

# Secțiunea de simulare live
st.subheader("📡 Live Sensor Data: Bridge Pillar 4")

# Butoanele interactive pentru juriu
col1, col2 = st.columns(2)
with col1:
    if st.button("🚨 Injectează Anomalie (Simulează Fisură)", type="primary"):
        st.session_state.fisura_activa = True
with col2:
    if st.button("🔄 Resetează Senzorii"):
        st.session_state.fisura_activa = False

# Generarea axei de timp
t = np.linspace(0, 10, 250)

# Logica de afișare a semnalului
if not st.session_state.fisura_activa:
    # Semnal NORMAL (Frecvență stabilă, zgomot redus)
    signal = np.sin(2 * np.pi * 1.5 * t) + np.random.normal(0, 0.1, 250)
    
    st.line_chart(signal)
    st.success("✅ System Status: Stable. No anomalies detected in natural frequency.")
else:
    # Semnal cu ANOMALIE (Frecvență modificată, zgomot masiv și un "spike" de energie care arată ruptura)
    # Zgomot de fond mai mare + schimbare de frecvență + un impact brusc la jumătatea graficului
    signal = np.sin(2 * np.pi * 1.1 * t) + np.random.normal(0, 0.6, 250) + np.where(t > 5, np.random.normal(0, 2.5, 250), 0)
    
    st.line_chart(signal)
    st.error("⚠️ CRITICAL ALERT: Micro-crack detected in Pillar 4! Structural rigidity compromised. AI predicts asymmetrical collapse in 47 days if unattended.")
    
    # Efect vizual de încărcare pentru simularea "AI-ului"
    st.progress(100, text="Initiating Emergency Protocol & Digital Twin Simulation...")
