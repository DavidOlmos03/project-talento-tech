import streamlit as st
import pandas as pd


def render():

    st.title("Upload Data")
    # Download the dataset from Google Drive
    st.write("**You can download the dataset here:**")
    st.markdown(
        """
        <a href="https://drive.google.com/drive/folders/1nH_kTb_M76YXgAztKm_xlIXy1NGUkqrK?usp=sharing" target="_blank">
            <button style="background-color: red; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 5px; cursor: pointer;">
                Open Drive Folder
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.write("\n")
    # Upload a file
    st.write("**Here you can upload your dataset for analysis.**")
    
    if "uploaded_files" not in st.session_state:
        st.session_state["uploaded_files"] = []  # Save the DataFrames
        st.session_state["uploaded_filenames"] = []  # Save the filenames
        
    st.title("Upload multiple CSV files")

    # Load multiple CSV files
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv", key="file_uploader")
    
    if uploaded_file:
        # Read a CSV file and add to the list
        try:
            st.session_state["uploaded_filenames"].append(uploaded_file.name)

            data = pd.read_csv(uploaded_file)
            st.session_state["uploaded_files"].append(data)
            st.success(f"File {uploaded_file.name} uploaded successfully.")
        except Exception as e:
            st.error(f"Error to upload the file: {e}")  
