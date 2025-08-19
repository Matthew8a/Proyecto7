import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
    <style>
    .stApp {
        background-color: #485878;
    }
    </style>
    """,
    unsafe_allow_html=True
)

car_data = pd.read_csv("vehicles_us.csv")

st.header("Bienvenido al Proyecto 7", divider="gray")
st.write("Creado por: Mateo Ochoa")
st.header("TRIPLETEN", divider="gray")


styled_df = car_data.sample(25).style.set_properties(**{
    'background-color': 'lightblue',
    'color': 'black',
    'border-color': 'white'
})
data_frame = st.checkbox("Visualiza una muestra de la tabla de datos")
if data_frame:
    st.dataframe(styled_df)

check_hist = st.checkbox("Genera un histograma")  # Cambio a un boton

if check_hist:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    histo = px.histogram(car_data, x="odometer",
                         color_discrete_sequence=px.colors.qualitative.Pastel)
    histo.update_layout(plot_bgcolor="#073E6B", paper_bgcolor="#073E6B")
    # Uso de streamlit en lugar de .show() de plotly
    st.plotly_chart(histo, use_container_width=True)

check_disp = st.button("Genera un gráfico de dispersión")

if check_disp:
    st.write("Creacion de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches")
    disp = px.scatter(car_data, x="odometer", y="price")
    disp.update_layout(plot_bgcolor="#073E6B", paper_bgcolor="#073E6B")
    st.plotly_chart(disp)  # Uso de streamlit en lugar de .show() de plotly
