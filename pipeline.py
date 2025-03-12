import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:141099@localhost:5432/postgres')

# Leitura do arquivo CSV
df = pd.read_csv('IOT-temp.csv')

# Inserção dos dados no banco
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
print("Dados inseridos no banco de dados com sucesso!")