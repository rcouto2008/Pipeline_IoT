## 🚀 Pipeline de Dados com IoT e Docker

É um projeto de um pipeline de dados que processa leituras de temperatura de dispositivos IoT e armazena em um banco de dados PostgreSQL usando Docker . Ele utiliza Streamlit para a interface gráfica, PostgreSQL para armazenamento dos dados e Plotly para a criação de gráficos interativos.


## 🎯 Objetivo

O objetivo deste projeto é fornecer uma solução completa para monitorar e analisar dados de temperatura coletados por dispositivos IoT, desde a coleta e armazenamento até a visualização em um dashboard interativo.

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
├── dashboard.py          # Script do dashboard Streamlit

├── pipeline.py           # Script para processar e carregar os dados

├── IOT-temp.csv          # Conjunto de dados de leituras de temperatura

├── requirements.txt      # Dependências do projeto

├── README.md             # Documentação do projeto

└── screenshots/          # Capturas de tela do dashboard
 
.............├── avg_temp.png
    
.............├── leituras_por_hora.png
     
.............└── temp_max_min.png


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

Insight: Identifica quais dispositivos estão registrando temperaturas mais altas ou mais baixas.

2. Leituras por Hora do Dia
Exibe a contagem de leituras de temperatura por hora.

Insight: Revela os horários de pico de atividade dos dispositivos.

3. Temperaturas Máximas e Mínimas por Dia
Apresenta as temperaturas máximas e mínimas registradas a cada dia.

Insight: Ajuda a identificar variações extremas de temperatura.


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

1. Temperaturas Mais Altas em Determinados Dispositivos
   O dispositivo 01 registrou a maior temperatura média (23.5°C), enquanto o dispositivo 03 teve a menor média (19.8°C).

   O que isso significa?

   O dispositivo 01 pode estar mais quente devido à falta de ventilação, exposição ao sol ou alta ocupação.

   O dispositivo 03 pode estar em uma área mais fresca ou ter um sistema de climatização mais eficiente.

   Ação sugerida:

   Verificar a localização e o funcionamento dos dispositivos 01.

   Considerar a instalação de ventiladores ou ajustes no sistema de ventilação.

2. Horário de Pico de Leituras
   O período entre 10h e 14h concentra a maioria das leituras, com um pico às 14h (7248 leituras).

   O que isso significa?

   Esse horário coincide com o período de maior atividade humana e uso de equipamentos.

   Pode indicar um aumento na demanda de energia ou na carga de trabalho dos dispositivos.

   Ação sugerida:

   Monitorar o desempenho dos dispositivos durante esse período para evitar sobrecargas.

   Avaliar a necessidade de ajustes no agendamento de tarefas para distribuir a carga.

3. Variações Significativas de Temperatura
   A temperatura máxima registrada foi 30°C, enquanto a mínima foi 15°C.

   O que isso significa?
 
   Essa grande variação pode indicar dias com condições climáticas extremas ou falhas nos dispositivos.

   Picos de temperatura podem afetar o conforto térmico e o consumo de energia.

   Ação sugerida:

   Implementar alertas para temperaturas fora da faixa esperada.

   Verificar a calibração dos dispositivos em dias com variações extremas.

4. Padrões de Temperatura ao Longo do Dia
   As temperaturas tendem a subir durante o dia e cair à noite, seguindo um padrão esperado.

   O que isso significa?

   Esse comportamento é consistente com a variação natural da temperatura ambiente.

   Picos inesperados durante a noite podem indicar problemas, como falhas nos dispositivos ou mudanças bruscas no ambiente.

   Ação sugerida:

   Monitorar padrões anormais de temperatura durante a noite.

   Investigar possíveis causas, como ambientes internos e externos como portas, janelas abertas ,exposição ao tempo .

5. Comparação Entre Dispositivos
   Dispositivos em  diferentes lugares mostram variações significativas na temperatura média.

   O que isso significa?

   A localização dos dispositivos pode influenciar diretamente as leituras.

   dispositivos com maior exposição ao sol ou menor ventilação tendem a registrar temperaturas mais altas.

   Ação sugerida:

   Reavaliar a posição dos dispositivos para garantir leituras mais precisas.

   Considerar a instalação de sensores adicionais em áreas críticas.
   


## 📸 Capturas de Tela Dashboard

1. Média de Temperatura por Dispositivo
   
![newplot (1)](https://github.com/user-attachments/assets/ce1db83b-e096-41e3-8a39-9fd6929daa7a)



3. Leituras por Hora do Dia
   
![newplot (2)](https://github.com/user-attachments/assets/f84f0ffa-e589-40de-9010-5d97397820fc)



5. Temperaturas Máximas e Mínimas por Dia
   
![newplot (3)](https://github.com/user-attachments/assets/bdc46fb5-0085-46d4-b407-0ac4ca918562)

