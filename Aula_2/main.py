from BancoLib import Banco

bancoUfrpe=Banco("UABJ")
print(10*"-","BEM VINDO AO BANCO",10*"-")
print("Menu de interações")
print("0 - sair")
print("1 - Criar uma conta")
print("2 - consulta saldo da conta")
print("3 - depositar na conta")
print("4 - Sacar da conta")
print("5 - render poupança")
print("6 - render bonûs")
print(20*"-")

escolha=int(input("digite a opção desejada: "))

while escolha>0:
    if escolha==1:
        #criar uma conta
        print("1- conta corrente")
        print("2- conta poupança")
        print("3 - conta bonificada")
        opcao=int(input("Digite o tipo da conta: "))
        if opcao ==1:
            print("cirando sua conta, gentileza aguardar...")
            numConta=bancoUfrpe.criarConta()
        elif opcao==2:
            
            percentual=int(input("digite quanto gostaria de render: "))
            numConta=bancoUfrpe.criarPoupanca(percentual)
        else:
            print("cirando sua conta, gentileza aguardar...")
            numConta=bancoUfrpe.criarContaBonificada()
        print("Conta criada ", numConta)
        print(20*"-")
    elif escolha ==2:
       
        numConta=int(input("digite o numero da conta: "))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("Seu saldo é: ",saldo)
        print(20*"-")
    elif escolha ==3:
       
        numConta=int(input("digite o numero da conta: "))
        valor=int(input("digite o valor que gostaria de depositar na conta: "))
        saldo = bancoUfrpe.depositar(numConta,valor)
        print("Valor depositado")
        print(20*"-")

    elif escolha ==4:
       
        numConta=int(input("digite o numero da conta: "))
        valor=int(input("digite o valor que gostaria de sacar na conta: "))
        resp = bancoUfrpe.sacar(numConta,valor)
        print(20*"-")
        if resp :
            print("valor sacado")
        else:
            print("valor insuficiente")
    elif escolha==5:
        numConta=int(input("digite o numero da conta: "))
        resp=bancoUfrpe.renderPoupanca(numConta)
        if resp:
            print("Poupança com novo saldo")
        else:
            print("A conta não é poupança ou não existe")
        print(20*"-")
    elif escolha==6:
        numConta=int(input("digite o numero da conta bonificada: "))
        resp=bancoUfrpe.renderCBonificada(numConta)
        if resp:
            print("Bonificada com novo saldo")
        else:
            print("A conta não é do tipo Bonificada ou não existe: ") 
        print(20*"-")     
    escolha=int(input("digite a opção desejada: "))
