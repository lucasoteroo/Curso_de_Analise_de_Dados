import random

class Conta():
    def __init__(self, numConta):
        self.numero=numConta
        self.saldo=0
        self.bonus=0
        

    def deposite(self,valor):
        self.saldo= self.saldo+ (valor-valor*0.1)
        self.bonus=valor*0.0001
            

    def sacar(self,valor):
        if self.saldo>= valor:
            self.saldo= self.saldo - valor
            return True
        else:
            return False

class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo* (0.01*self.percentual)
           

    def __init__(self, numConta, percentual):
        self.percentual=percentual
        super().__init__(numConta)

   

class ContaBonificada(Conta):

    def renderB(self):
        self.bonus=self.bonus
        self.saldo=self.saldo+self.bonus
        self.bonus=0

        
class Banco():

    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num=random.randint(0,1000)
        c=Conta(num)
        self.contas.append(c)
        return num
    
    def criarPoupanca(self,percentual):
        num=random.randint(0,1000)
        p=Poupanca(num,percentual)
        self.contas.append(p)
        return num

    def criarContaBonificada(self):
        num=random.randint(0,1000)
        cb=ContaBonificada(num)
        self.contas.append(cb)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero==numConta:
                return conta.saldo
        return -1
        
    def depositar(self, numConta,valor):
        for conta in self.contas:
            if conta.numero==numConta: 
                conta.deposite(valor)

    def sacar(self, numConta,valor):
        for conta in self.contas:
            if conta.numero==numConta:
                return conta.sacar(valor)
            
    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero==numConta and isinstance(i,Poupanca):
                    i.render()
                    return True
        return False
    
    def renderCBonificada(self, numConta):
        for i in self.contas:
            if i.numero==numConta and isinstance(i,ContaBonificada):
                    i.renderB()
                    return True
        return False
