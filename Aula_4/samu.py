import pandas as pd
import numpy
from scipy import stats

dados = pd.read_csv('ocorrencias-22.csv', sep=';',
                       on_bad_lines='skip', low_memory=False)
#a linha acima usa o pandas para ler o arq csv, no qual as linhas são separadas por ';' e onde não for a leitura 'skipa', também não use limitadores de memória

#Avaliação 1
dados.dropna(subset=['idade'],inplace=True)
#a linha acima usa o dropna retornando só o que for número em idade
dados["idadeNormalizada"]=pd.to_numeric(dados["idade"],errors='coerce')
medianaIdade= dados["idadeNormalizada"].median()
mediaIdade= dados["idadeNormalizada"].mean()

print("A mediana das idades de pessoas que solicitaram o SAMU em 2022 é: ",medianaIdade)
print("A média das idades de pessoas que solicitaram o SAMU em 2022 é: ",mediaIdade)

#Avaliação 2

dados.dropna(subset=['idade'],inplace=True)
#aqui tem mais um dropna pois para testar precisei comentar as outras avaliações
feminino= dados[dados['sexo'] == 'FEMININO']['idade']
masculino= dados[dados['sexo'] == 'MASCULINO']['idade']
feminino=pd.to_numeric(feminino,errors='coerce')
masculino=pd.to_numeric(masculino,errors='coerce')

t_stat, p_value=stats.ttest_ind(feminino,masculino, equal_var=False)
print("t-teste ", t_stat)
print(p_value)

medianaFem= feminino.median()
medianaMasc= masculino.median()
mediaFem = feminino.mean()
mediaMasc= masculino.mean()

print("A média das idades de mulheres que solicitaram o SAMU em 2022 é: ",mediaFem)
print("A média das idades de Homens que solicitaram o SAMU em 2022 é: ",mediaMasc)
print("A medina das idades de mulheres que solicitaram o SAMU em 2022 é: ",medianaFem)
print("A mediana das idades de mulheres que solicitaram o SAMU em 2022 é: ",medianaMasc)

#Interpret results
alpha = 0.05
if p_value > alpha:
    print("não rejeito a hipótese nula")
else:
    print("meus testes representam uma acertividade em cima de 95% dos dados")


#Avaliação 3

Bairros=dados['bairro'].value_counts(dropna=False, sort=True, ascending=True)
#na linha acima verifico na coluna tal quantas vezes cada objeto se repete e retorno ele em ordem crescente
print("Os bairros no qual o SAMU mais foi solicitado em 2022 foram: ",Bairros)

#Avaliação 4

Motivos=dados['subtipo'].value_counts(dropna=False, sort=True, ascending=True)
#na linha acima verifico na coluna tal quantas vezes cada objeto se repete e retorno ele em ordem crescente
print("Os motivos no qual o SAMU mais foi solicitado em 2022 foram: ",Motivos)

#Avaliação 5
horarios=dados['hora_minuto'].value_counts(dropna=False, sort=True, ascending=True)
#na linha acima verifico na coluna tal quantas vezes cada objeto se repete e retorno ele em ordem crescente
print("As horas nas quais o serviço no SAMU mais foi solitado, foram: ",horarios)
