import random
import sqlite3
import mysql.connector

# Cria uma conexão com o banco de dados
cnx = mysql.connector.connect(user='sql10591880',
                              password='Uj8canyVDM',
                              host='sql10.freemysqlhosting.net',
                              port=3306,
                              database='sql10591880')

# Cria um cursor para executar consultas
cursor = cnx.cursor()

class Conta():
    def __init__(self, numConta):
        self.number = numConta
        self.saldoConta = 0
       

   # def deposite(self, valor):
    #    self.saldoConta = self.saldoConta + valor

    #def sacar(self, valor):
     #   if self.saldoConta >= valor:
      #      self.saldoConta = self.saldoConta - valor
        #    return True
       # else:
         #   return False


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS BANC (NUMECONTA INT, SALDO REAL)''') 
        #aqui foi criado a tabela banco com dois parametros e ela só é criada se nenhuma outra tabela com o mesmo nome existe
        self.cnx.commit()
        

    def getNome(self):
        return self.nome

    def criarConta(self):
        numero = random.randint(0, 1000)
        self.cursor.execute(f'''INSERT INTO BANC (NUMECONTA, SALDO) VALUES ({numero},0) ''')
        #na linha acima o cursor está inserindo dois objetos na tabela BANCO, o numconta tem como dado o número aleatório gerado acima
        #e o saldoConta começa zerado.
        self.cnx.commit()
        return numero

    def consultaSaldo(self, numConta):
        self.cursor.execute(f'''SELECT SALDO FROM BANC WHERE NUMECONTA = {numConta} ''')
        #aqui estou selecionando o saldo na tabela banc de acordo com o numConta
        saldoConta= self.cursor.fetchone()
        #aqui saldoConta recebe o saldo daquela respectiva conta (numConta)
        if saldoConta != 0: #como saldoConta recebe o saldo da conta respectiva mas na primeira iteração ela tem valor "none"
            #essa condição será sempre verdadeira.
            return saldoConta[0]
        else:
            return -1
    
    def depositar(self, numConta, valor):
        self.cursor.execute(f'''UPDATE BANC SET SALDO = SALDO + {valor} WHERE NUMECONTA = {numConta} ''')
        #aqui sobrescrevo na tabela o saldoConta após o deposito onde nesse método faço a operação para atualizar o mesmo
        
        self.cnx.commit()

    def sacar(self, numConta, valor):
        self.cursor.execute(f'''SELECT SALDO FROM BANC WHERE NUMECONTA = {numConta} ''')
        #aqui estou selecionando o saldo na tabela banc de acordo com o numConta
        saldoConta= self.cursor.fetchone()
        #saldoConta recebe registro tal naquela linha
        if saldoConta and saldoConta[0]>= valor:
            self.cursor.execute(f'''UPDATE BANC SET SALDO = SALDO - {valor} WHERE NUMECONTA = {numConta} ''')
            #aqui sobrescrevo na tabela o saldoConta após o saque e retorno esse valor pós operação
            self.cnx.commit()
            return True
        else:
            print("Saldo insuficiente para esse saque, gentileza consultar saldo antes do saque ")
            return False
