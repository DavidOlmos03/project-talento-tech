import streamlit as st

def render():
    st.title("Data Visualization")
    
    # Show uploaded files
    if "uploaded_files" in st.session_state and st.session_state["uploaded_files"]:
        st.header("Files Uploaded")
        for idx, data in enumerate(st.session_state["uploaded_files"]):
            st.subheader(f"File {idx + 1}")
            st.write(f"Filename: {st.session_state['uploaded_filenames'][idx]}")
            st.dataframe(data, use_container_width=True)
    else:
        st.write("Please upload a dataset in the 'Upload Data' section.")