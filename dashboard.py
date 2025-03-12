import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:141099@localhost:5432/postgres')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Carregar dados das views
df_avg_temp = load_data('avg_temp_por_dispositivo')
df_leituras_hora = load_data('leituras_por_hora')
df_temp_max_min = load_data('temp_max_min_por_dia')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
fig1 = px.bar(
    df_avg_temp,
    x='room_id/id',
    y='avg_temp',
    labels={'room_id/id': 'Dispositivo', 'avg_temp': 'Temperatura Média (°C)'},
    text='avg_temp'
)
fig1.update_traces(textposition='outside')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')

# Garante que os dados estão ordenados por hora
df_leituras_hora = df_leituras_hora.sort_values('hora')

fig2 = px.line(
    df_leituras_hora,
    x='hora',
    y='contagem',
    labels={'hora': 'Hora do Dia', 'contagem': 'Número de Leituras'},
    title='Leituras por Hora do Dia',
    markers=True,
    range_x=[0, 23],  # Define o intervalo do eixo X (0 a 23 horas)
    range_y=[0, df_leituras_hora['contagem'].max() + 100],  # Ajusta o eixo Y para evitar valores muito altos
    text='contagem'  # Exibe os valores de contagem nos pontos
)

# Melhora a legibilidade dos rótulos do eixo X
fig2.update_xaxes(
    tickvals=list(range(24)),  # Define os valores do eixo X (0 a 23)
    ticktext=[str(i) for i in range(24)]  # Rótulos do eixo X
)

# Exibe o gráfico
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')

# Garante que os dados estão ordenados por data
df_temp_max_min = df_temp_max_min.sort_values('data')

fig3 = px.line(
    df_temp_max_min,
    x='data',
    y=['temp_max', 'temp_min'],
    labels={'data': 'Data', 'value': 'Temperatura (°C)'},
    title='Temperaturas Máximas e Mínimas por Dia',
    markers=True,
    line_shape='linear',
    range_y=[df_temp_max_min['temp_min'].min() - 5, df_temp_max_min['temp_max'].max() + 5]
)

# Melhora a legibilidade dos rótulos do eixo X
fig3.update_xaxes(
    tickformat='%Y-%m-%d',  # Formato da data
    tickangle=45  # Inclina os rótulos para melhor visualização
)

# Exibe o gráfico
st.plotly_chart(fig3)