import streamlit as st
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from io import BytesIO

# Components for data visualization
from components.wind_rose import wind_rose, predict_wind_rose
# utils
from utils.predict_wind_rose_model import predict_wind_rose_model

import streamlit as st

def render():
    st.title("Data Visualization")
    if "uploaded_data" in st.session_state and "uploaded_filename" in st.session_state:
        data = st.session_state["uploaded_data"]
        filename = st.session_state["uploaded_filename"]
        if filename == "20.csv" or filename == "19.csv" or filename == "18.csv":
            # Verificar salida de wind_rose
            wind_rose_image = wind_rose(data)
            if wind_rose_image is None:
                st.error("Error: La visualización Wind Rose Real no se generó correctamente.")
                return

            # Verificar salida de predicción
            with st.spinner("Generando predicciones. Esto puede tardar unos momentos..."):
                direccion_pred, velocidad_pred = predict_wind_rose_model(data)
                if direccion_pred is None or velocidad_pred is None:
                    st.error("Error: La predicción del modelo falló.")
                    return
                predict_wind_rose_image = predict_wind_rose(direccion_pred, velocidad_pred)
                if predict_wind_rose_image is None:
                    st.error("Error: La visualización de la predicción no se generó correctamente.")
                    return

            # Mostrar las imágenes en una sola fila de manera responsive
            col1, col2 = st.columns(2)
            with col1:
                st.title("Wind Rose")
                st.image(wind_rose_image, caption="Wind Rose Real", use_container_width=True)
            with col2:
                st.title("Wind Rose Predicted")
                st.image(predict_wind_rose_image, caption="Wind Rose Prediction", use_container_width=True)
        else:
            st.write("No specific visualization available for this file.")
    else:
        st.write("Please upload a dataset in the 'Upload Data' section.")
