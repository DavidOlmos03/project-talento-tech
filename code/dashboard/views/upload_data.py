import streamlit as st
import pandas as pd

def render():
    st.title("Upload Data")
    st.write("Here you can upload your dataset for analysis.")
    uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.session_state["uploaded_data"] = data
        st.session_state["uploaded_filename"] = uploaded_file.name
        st.dataframe(data)


