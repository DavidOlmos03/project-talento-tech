from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def predict_wind_rose_model(data):
    filtered_data = data[['direccion_viento', 'velocidad_viento', 'presion_barometrica', 'temperatura']].dropna()

    # Tomar una muestra de 50,000 registros para el análisis
    sample_data = filtered_data.sample(n=50000, random_state=42)

    # Dividir en características (X) y objetivos (y)
    X = sample_data[['presion_barometrica', 'temperatura']]
    y_direccion = sample_data['direccion_viento']  # Objetivo 1: Dirección del viento
    y_velocidad = sample_data['velocidad_viento']  # Objetivo 2: Velocidad del viento

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_direccion_train, y_direccion_test, y_velocidad_train, y_velocidad_test = train_test_split(
        X, y_direccion, y_velocidad, test_size=0.2, random_state=42
    )

    # Crear y entrenar modelos Random Forest
    rf_direccion = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_velocidad = RandomForestRegressor(n_estimators=100, random_state=42)

    rf_direccion.fit(X_train, y_direccion_train)
    rf_velocidad.fit(X_train, y_velocidad_train)

    # Realizar predicciones
    direccion_pred = rf_direccion.predict(X_test)
    velocidad_pred = rf_velocidad.predict(X_test)

    # Calcular métricas de evaluación
    mse_direccion = mean_squared_error(y_direccion_test, direccion_pred)
    r2_direccion = r2_score(y_direccion_test, direccion_pred)

    mse_velocidad = mean_squared_error(y_velocidad_test, velocidad_pred)
    r2_velocidad = r2_score(y_velocidad_test, velocidad_pred)


    # Return the predictions
    return direccion_pred, velocidad_pred

