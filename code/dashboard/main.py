import streamlit as st
from views import home, upload_data, data_visualization, statistical_analysis, machine_learning
import matplotlib.pyplot as plt

def main():
    # Set page configuration
    st.set_page_config(page_title="Responsive Menu for Data Analysis", layout="wide")

    # Define the menu options
    menu_options = {
        "Home": home.render,
        "Upload Data": upload_data.render,
        "Data Visualization": data_visualization.render,
        "Statistical Analysis": statistical_analysis.render,
        "Machine Learning": machine_learning.render,
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
