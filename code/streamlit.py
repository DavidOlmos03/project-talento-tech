import streamlit as st
import pandas as pd
import altair as alt

# Load the data
file_path = "../project_course/posiciones_liga_2024_1.csv"
df = pd.read_csv(file_path)

# Initial setup
st.title("League 2024 Analysis")
st.sidebar.title("Filter Options")
st.write("This interactive dashboard allows you to analyze the standings of football teams in the 2024 league.")

# Show full table
if st.checkbox("Show full data table"):
    st.dataframe(df)

# Filters by team and points range
st.sidebar.subheader("Filters")
team = st.sidebar.multiselect("Select teams", options=df["Equipo"].unique())
min_points, max_points = st.sidebar.slider(
    "Points range",
    min_value=int(df["Puntos"].min()),
    max_value=int(df["Puntos"].max()),
    value=(int(df["Puntos"].min()), int(df["Puntos"].max()))
)

# Apply filters
filtered_df = df[
    ((df["Equipo"].isin(team)) if team else True) &
    (df["Puntos"] >= min_points) &
    (df["Puntos"] <= max_points)
]
st.write(f"{len(filtered_df)} teams displayed after applying filters:")
st.dataframe(filtered_df)

# Key metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Teams", len(df))
col2.metric("Max Points", df["Puntos"].max())
col3.metric("Min Points", df["Puntos"].min())

# Points per team chart
st.subheader("Chart: Points per Team")
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X("Equipo", sort="-y"),
    y="Puntos",
    color="Equipo"
).properties(width=700, height=400)
st.altair_chart(chart, use_container_width=True)

# Goal difference chart
st.subheader("Chart: Goal Difference")
goal_diff_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x=alt.X("Equipo", sort="-y"),
    y="Dif. Gol",
    color="Equipo"
).properties(width=700, height=400)


if 'scatter_plot' in locals():
    st.altair_chart(scatter_plot, use_container_width=True)
else:
    st.error("La gráfica de dispersión no está definida.")

