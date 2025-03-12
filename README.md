# 🚀 Pipeline de Dados com IoT e Docker

Este projeto é um pipeline de dados que processa leituras de temperatura de dispositivos IoT, armazena os dados em um banco PostgreSQL usando Docker e visualiza os dados em um dashboard interativo com Streamlit.

---

## 🎯 Objetivo

O objetivo deste projeto é criar um pipeline de dados completo, desde a coleta e armazenamento até a visualização, utilizando tecnologias modernas como Docker, PostgreSQL, Python e Streamlit.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Para processamento de dados e criação do dashboard.
- **PostgreSQL**: Banco de dados para armazenamento das leituras de temperatura.
- **Docker**: Para containerização do banco de dados.
- **Streamlit**: Framework para criação do dashboard interativo.
- **Pandas**: Biblioteca para manipulação de dados.
- **Plotly**: Para criação de gráficos interativos.

---

## 📂 Estrutura do Projeto

pipeline-iot/
├── dashboard.py # Script do dashboard Streamlit
├── pipeline.py # Script para processar e carregar os dados
├── IOT-temp.csv # Conjunto de dados de leituras de temperatura
├── requirements.txt # Dependências do projeto
├── README.md # Documentação do projeto
└── venv/ # Ambiente virtual Python


---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Docker**: [Instale o Docker](https://www.docker.com/).
- **Python**: [Instale o Python](https://www.python.org/).
- **Git**: [Instale o Git](https://git-scm.com/).

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone git clone https://github.com/rcouto2008/Pipeline_IoT.git
   cd pipeline-iot


2. **Crie o contêiner PostgreSQL**:
   ```bash
   docker run --name postgres-iot -e POSTGRES_PASSWORD=senha_correta -p 5432:5432 -d postgres

3. **Configure o ambiente virtual Python**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac

4. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt  

5. **Processe e carregue os dados no banco**:

   ```bash
   python pipeline.py

6. **Execute o dashboard**:

   ```bash
   streamlit run dashboard.py

O dashboard estará disponível em: http://localhost:8501.


## 📊 Visualizações

O dashboard contém três gráficos interativos:

1. Média de Temperatura por Dispositivo
Mostra a temperatura média de cada dispositivo IoT.

O dispositivo sala-01 tem a maior temperatura média (23.5°C), possivelmente devido à falta de ventilação.

2. Leituras por Hora do Dia
Exibe a contagem de leituras de temperatura por hora.
 O horário com maior número de leituras é às 14h, com 7248 leituras, indicando um pico de atividade.

3. Temperaturas Máximas e Mínimas por Dia
Apresenta as temperaturas máximas e mínimas registradas a cada dia.
A temperatura máxima registrada foi 30°C, enquanto a mínima foi 15°C, mostrando variações significativas.

## 🗂️ Views SQL

Foram criadas as seguintes views no PostgreSQL para facilitar as análises:

1. Média de temperatura por dispositivo
   ```sql

   CREATE VIEW avg_temp_por_dispositivo AS
   SELECT "room_id/id", AVG(temp) AS avg_temp
   FROM temperature_readings
   GROUP BY "room_id/id";

2. Contagem de leituras por hora
   ```sql
   CREATE VIEW leituras_por_hora AS
   SELECT EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora, COUNT(*) AS contagem
   FROM temperature_readings
   GROUP BY hora;
3. Temperaturas máximas e mínimas por dia
   ```sql
   CREATE VIEW temp_max_min_por_dia AS
   SELECT DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min
   FROM temperature_readings
   GROUP BY data;

## 🔍 Insights
Temperaturas Mais Altas em Determinados Dispositivos:

O dispositivo sala-01 registrou a maior temperatura média (23.5°C). Isso pode indicar que essa sala está mais quente que as outras, possivelmente devido à falta de ventilação ou à localização do dispositivo.

Horário de Pico de Leituras:

O período entre 10h e 14h concentra a maioria das leituras, com um pico às 14h (7248 leituras). Isso sugere que os dispositivos estão mais ativos durante a tarde, o que pode estar relacionado ao aumento do uso de equipamentos ou à maior movimentação de pessoas.

Variações Significativas de Temperatura:

A temperatura máxima registrada foi 30°C, enquanto a mínima foi 15°C. Essa grande variação pode ser útil para identificar dias com condições extremas e ajustar sistemas de climatização ou alertas.

Padrões de Temperatura ao Longo do Dia:

As leituras mostram que as temperaturas tendem a subir durante o dia e cair à noite, seguindo um padrão esperado. No entanto, picos inesperados podem indicar problemas, como falhas nos dispositivos ou mudanças bruscas no ambiente.

## 📸 Capturas de Tela Dashboard

1. Média de Temperatura por Dispositivo
   
![newplot (1)](https://github.com/user-attachments/assets/356216cf-ca0d-4892-a680-d2c32b54f061)


3. Leituras por Hora do Dia
   
![newplot (2)](https://github.com/user-attachments/assets/2e100f85-97e2-4e8b-ade7-4c95679065a0)


5. Temperaturas Máximas e Mínimas por Dia
   
![newplot (3)](https://github.com/user-attachments/assets/4e14c4bc-2b90-477a-ad61-f6f4bba59c57)

