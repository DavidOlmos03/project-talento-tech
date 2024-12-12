import streamlit as st

def render():
    st.title("Statistical Analysis")
    st.write("Here you can perform statistical analysis on your dataset.")

    st.subheader("Spanish")
    st.write("""
        Consideraciones Estadísticas al Analizar Datos de Sensores Eólicos <br>
        
        - El análisis de datos provenientes de sensores eólicos, como el sensor registrado en el archivo 18.csv, presenta desafíos únicos debido a la naturaleza compleja de las variables involucradas, como la velocidad y la dirección del viento. Estas variables suelen estar influenciadas por fenómenos estocásticos, patrones estacionales, y características geográficas, lo que complica su modelado.<br>

        Predicción de la Dirección del Viento:<br>

        - En la predicción de la dirección del viento utilizando Random Forest Regression, los resultados obtenidos muestran un Error Cuadrático Medio (MSE) de 3938.75 y un coeficiente de determinación (R²) de 0.56. Estos valores indican que el modelo tiene limitaciones para capturar adecuadamente los patrones subyacentes de esta variable. Esto puede deberse a:

        - La naturaleza circular de la dirección del viento, donde las transiciones entre 0° y 360° generan discontinuidades que los modelos basados en regresión no manejan bien.
        Alta variabilidad y ruido en los datos medidos, que puede dificultar la identificación de patrones consistentes.<br>
        
        Predicción de la Velocidad del Viento:<br>

        - Por otro lado, la predicción de la velocidad del viento muestra resultados significativamente mejores, con un MSE de 0.90 y un R² de 1.00, lo que indica que el modelo puede capturar los patrones de esta variable con alta precisión. La velocidad del viento tiende a ser más continua y menos afectada por las discontinuidades inherentes a las variables circulares, lo que facilita su modelado.<br>
    """, unsafe_allow_html=True)

    st.subheader("English")
    st.write("""
        Considerations on Statistical Analysis of Sensor Data <br>
        - The analysis of data from sensors, such as the sensor recorded in the file 18.csv, presents unique challenges due to the complex nature of the variables involved, such as the wind speed and direction. These variables are often influenced by statistical phenomena, seasonal patterns, and geographic features, which complicate their modeling.

        Wind Direction Prediction:<br>

        - In the prediction of wind direction using Random Forest Regression, the results obtained show an MSE of 3938.75 and an R² of 0.56. These values indicate that the model has limitations in capturing the underlying patterns of this variable. This may be due to:

        - The circular nature of wind direction, where the transitions between 0° and 360° generate discontinuities that the regression-based models cannot handle well.
        High variability and noise in the data measured, which may make it difficult to identify consistent patterns.
        
        Wind Speed Prediction:

        - On the other hand, the prediction of wind speed shows better results, with an MSE of 0.90 and an R² of 1.00, indicating that the model can capture the patterns of this variable with high precision. The wind speed tends to be more continuous and less affected by the discontinuities inherent to circular variables, making it easier to model.        
    """, unsafe_allow_html=True)