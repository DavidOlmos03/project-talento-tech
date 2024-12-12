import streamlit as st
from views import home, upload_data, data_visualization, statistical_analysis, machine_learning, bibliography
import matplotlib.pyplot as plt
import utils.menu as util

#Página de presentación
st.set_page_config(
    page_title="Data Science Project - Wind Rose Prediction",
    page_icon=":tornado:",
    initial_sidebar_state='expanded',
    layout="wide"
)

def main():
    #llamamos a las otras páginas   
    util.generarMenu()
    # Define the menu options
    menu_options = {
        "Home": home.render,
        "Upload Data": upload_data.render,
        "Data Visualization": data_visualization.render,
        "Statistical Analysis": statistical_analysis.render,
        "Machine Learning": machine_learning.render,
        "Bibliography": bibliography.render,
    }

    # Sidebar menu
    st.sidebar.title("Navigation Menu")
    selected_option = st.sidebar.radio("Choose a section:", list(menu_options.keys()))

    # Render the selected view
    menu_options[selected_option]()

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.write("Data Analysis Dashboard \u00a9 2024")


if __name__ == "__main__":
    main()
