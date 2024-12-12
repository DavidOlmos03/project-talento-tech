import streamlit as st

def bibliography():
    st.title("Bibliography")
    st.write(
        """
        [1] Data Science Project - Talento Tech.<br>
        Restrepo, G., Mendoza, S., Giraldo, A., Soriano, S., Cano, D., Rojas, J., Ruiz Olmos, J. (2024).<br>
        Data Science Project - Wind Rose Prediction.<br>
        """,
        unsafe_allow_html=True
    )

    # Google Drive button with logo
    google_drive_button = """
    <a href="https://drive.google.com/drive/folders/1ANIlQGzCSmlJTndpAjG9w5joGTZmYX4f?usp=sharing" target="_blank" style="text-decoration: none;">
        <button style="display: flex; align-items: center; background-color: #4285F4; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Google_Drive_logo.png" alt="Google Drive" style="height: 20px; margin-right: 10px;">
            Open Google Drive
        </button>
    </a>
    """

    st.markdown(google_drive_button, unsafe_allow_html=True)



    st.write(
        """
        <br>
        [2] Wind Rose Prediction: Ingénieria de la Energía Eólica.<br> 
        Villarrubia, M. (2013). <br>
        Facultad de Física - Universidad de Barcelona. <br>
        """,
        unsafe_allow_html=True
    )