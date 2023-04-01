import sqlite3
import pandas as pd
import numpy as np

# Conectar ao banco de dados SQLite Studio
conn = sqlite3.connect('pet.db')
cursor = conn.cursor()

query= "SELECT * FROM dados"
dados=pd.read_sql_query(query,conn)

#"Carga - Equalização" | Ah carga	
#seleciona a penúltima linha do DataFrame "dados" onde o valor na coluna "Step" é igual a 3 e armazena essa linha na variável "linha".
linha = dados.loc[dados['Step'] == 3].iloc[-2]
#print(linha)  

#aqui retorna a última linha do ste n
#linha = dados.loc[dados['Step'] == 6].groupby('Step').last()

#CAPACIADES NOMINAIS
# seleciona as colunas "x2" e "x3" do DataFrame "dados" e as armazena em "dados_não_nulos".
dados_nao_nulos = dados[['x2', 'x3']][dados[['x2', 'x3']].notnull().any(axis=1)]
#print(dados_nao_nulos)

#PEUKERT
# seleciona as colunas "Peukert1_75V" e "x4" do DataFrame "dados" e as armazena em "peukert".
peukert=dados[['Peukert1_75V','x4']]
print(peukert)

query2= "SELECT * FROM form_prot"
dados2=pd.read_sql_query(query2,conn)


#   AQUI RETORNO O VALOR PARA CARGA FORMÇÃO
dados2['AhCha'] = dados2['AhCha'].str.replace(",", ".")
dados2['AhCha'] = dados2['AhCha'].replace('', np.nan)
dados2['AhCha'] = dados2['AhCha'].astype(float)
maior_AhCha = dados['AhCha'].max()

print(maior_AhCha)


conn.commit()
conn.close()
