import streamlit as st
from windrose import WindroseAxes
from io import BytesIO
import matplotlib.pyplot as plt

def wind_rose(data):
    fig, ax = plt.subplots()
    ax = WindroseAxes.from_ax()
    ax.bar(
        data['direccion_viento'], 
        data['velocidad_viento'], 
        normed=True, 
        opening=0.8, 
        edgecolor='white')
    ax.set_legend()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    # Cerrar la figura para liberar memoria
    plt.close(fig)
    
    # Retornar el buffer
    return buf

    #st.image(buf)


def predict_wind_rose(direccion_pred_y, velocidad_pred_y):
    fig, ax_pred = plt.subplots()
    ax_pred = WindroseAxes.from_ax()
    ax_pred.bar(
        direccion_pred_y,
        velocidad_pred_y,
        normed=True,
        opening=0.8,
        edgecolor='white'
    )
    ax_pred.set_legend()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    #st.image(buf)
    # Cerrar la figura para liberar memoria
    plt.close(fig)
    
    # Retornar el buffer
    return buf