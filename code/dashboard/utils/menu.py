import streamlit as st
from PIL import Image
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "../imgs/forest_logo.png")

def generarMenu():
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1:
            image = Image.open(image_path)
            st.image(image, use_container_width=False, width=50 )
        with col2:
            st.header('Wind Rose')

        # st.page_link(home, label='Inicio', icon='🏠')
        # st.page_link('views/upload_data.py', label='Upload Data', icon='📂')
        # st.page_link('views/data_visualization.py', label='Data Visualization', icon='📊')
        # st.page_link('views/statistical_analysis.py', label='Statistical Analysis', icon='📊')
        # st.page_link('views/machine_learning.py', label='Machine Learning', icon='🧠')
        # st.page_link('views/bibliography.py', label='Bibliography', icon='📚')