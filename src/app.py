import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Predicción del Clima", page_icon="⛅", layout="centered")

st.title("🌤️ Predicción del Clima con IA")
st.write("Ajusta los valores para predecir si el clima será *soleado* o *lluvioso*.")

# === Cargar modelo y columnas ===
try:
    with open('modelo_clima.pkl', 'rb') as f:
        modelo_clima = pickle.load(f)

    with open('columnas_modelo.pkl', 'rb') as f:
        columnas = pickle.load(f)
except Exception as e:
    st.error("❌ Error al cargar el modelo. Asegúrate de tener los archivos `.pkl` correctamente guardados.")
    st.stop()

# === Entradas desde el usuario ===
precipitacion = st.slider("Precipitación (mm)", 0, 100, 10)
temp_max = st.slider("Temperatura Máxima (°C)", 10, 45, 30)
temp_min = st.slider("Temperatura Mínima (°C)", 0, 30, 20)
viento = st.slider("Velocidad del Viento (m/s)", 0, 20, 5)

# === Crear dataframe de entrada ===
entrada = pd.DataFrame([{
    'precipitacion': precipitacion,
    'temp_max': temp_max,
    'temp_min': temp_min,
    'viento': viento
}], columns=columnas)

# === Predicción ===
if st.button("Predecir Clima"):
    pred = modelo_clima.predict(entrada)[0]
    st.success(f"🌈 El modelo predice que el clima será: **{pred.upper()}**")
