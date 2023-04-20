import sqlite3
import pandas as pd
from datetime import datetime, timedelta

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('pet.db')

# Carrega a tabela do banco de dados em um DataFrame do pandas
consulta = pd.read_sql_query('SELECT * FROM dados', conn)

# Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
linha_especifica = consulta.loc[(consulta['Voltage'] == '1,750') & (consulta['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]

# Converte o formato de hora para número de horas com precisão de 3 casas decimais
linha_especifica['StepTime'] = pd.to_timedelta(linha_especifica['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

print("Valores Peukert para o Am 01 (CBI22-076), sendo StepTime(duração) e Current(corrente)")
print(" ")

# Imprime as linhas selecionadas
print(linha_especifica)
conn.close()

#-------------------------------------------------------

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('pet.db')

# Carrega a tabela do banco de dados em um DataFrame do pandas
consulta2 = pd.read_sql_query('SELECT * FROM peukert_dados', conn)

# Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
linha_especifica2 = consulta2.loc[(consulta2['Voltage'] == '1,75') & (consulta2['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]

# Converte o formato de hora para número de horas com precisão de 3 casas decimais
linha_especifica2['StepTime'] = pd.to_timedelta(linha_especifica2['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

# Imprime as linhas selecionadas
print(linha_especifica2)
conn.close()
