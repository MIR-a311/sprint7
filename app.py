import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de vehículos en EE.UU.")

# Mostrar una vista previa del DataFrame
st.write("Vista previa de los datos:")
st.write(df.head())

# Casilla para mostrar histograma
build_histogram = st.checkbox("Mostrar histograma de años del modelo")
if build_histogram:
    st.write("Histograma del año del modelo")
    fig = px.histogram(df, x='model_year', title='Distribución del Año del Modelo')
    st.plotly_chart(fig)

# Casilla para mostrar gráfico de dispersión
build_scatter = st.checkbox("Mostrar gráfico de dispersión precio vs. odómetro")
if build_scatter:
    st.write("Gráfico de dispersión: precio vs. odómetro")
    scatter = px.scatter(df, x='odometer', y='price',
                         title='Precio vs. Odómetro',
                         labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)'})
    st.plotly_chart(scatter)
    
    # Casilla para mostrar boxplot de precios por tipo de vehículo
build_boxplot = st.checkbox("Mostrar boxplot de precio por tipo de vehículo")
if build_boxplot:
    st.write("Boxplot de precio según tipo de vehículo")
    box = px.box(df, x='type', y='price',
                 title='Distribución del precio por tipo de vehículo',
                 labels={'type': 'Tipo de vehículo', 'price': 'Precio (USD)'})
    st.plotly_chart(box)