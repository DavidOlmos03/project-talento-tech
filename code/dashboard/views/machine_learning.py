import streamlit as st
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from io import BytesIO

# Components for data visualization
from components.wind_rose import wind_rose, predict_wind_rose
# utils
from utils.predict_wind_rose_model import predict_wind_rose_model

def render():
    st.title("Machine Learning")
    
    # Start the session_state list for stored processed files
    if "processed_files" not in st.session_state:
        st.session_state["processed_files"] = {}  # Dictionary to store processed files

    if "uploaded_files" in st.session_state and st.session_state["uploaded_files"]:
        for idx, data in enumerate(st.session_state["uploaded_files"]):
            filename = st.session_state["uploaded_filenames"][idx]
            # Process the new file
            if filename not in st.session_state["processed_files"]:
                st.subheader(f"Processing file {idx + 1}: {filename}")
                wind_rose_image = wind_rose(data)
                if wind_rose_image is None:
                    st.error(f"Error: La visualización Wind Rose Real no se generó correctamente para {filename}.")
                    continue
                
                with st.spinner("Generando predicciones. Esto puede tardar unos momentos..."):
                    direccion_pred, velocidad_pred = predict_wind_rose_model(data)
                    if direccion_pred is None or velocidad_pred is None:
                        st.error(f"Error: La predicción del modelo falló para {filename}.")
                        continue
                    
                    predict_wind_rose_image = predict_wind_rose(direccion_pred, velocidad_pred)
                    if predict_wind_rose_image is None:
                        st.error(f"Error: La visualización de la predicción no se generó correctamente para {filename}.")
                        continue
                
                # Save the result in the session_state
                st.session_state["processed_files"][filename] = {
                    "wind_rose_image": wind_rose_image,
                    "predict_wind_rose_image": predict_wind_rose_image
                }

            # Show the images in a responsive layout
            st.subheader(f"Results for file {idx + 1}: {filename}")
            col1, col2 = st.columns(2)
            with col1:
                st.title("Wind Rose")
                st.image(st.session_state["processed_files"][filename]["wind_rose_image"],
                        caption="Wind Rose Real", use_container_width=True)
            with col2:
                st.title("Wind Rose Predicted")
                st.image(st.session_state["processed_files"][filename]["predict_wind_rose_image"],
                        caption="Wind Rose Prediction", use_container_width=True)
    else:
        st.write("Please upload a dataset in the 'Upload Data' section.")
