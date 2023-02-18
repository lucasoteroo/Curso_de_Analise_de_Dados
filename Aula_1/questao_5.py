''' Faça uma função chamada calculaSalario que recebe como parâmetro o valor do salário bruto calcula o salário líquido.
 O salário líquido é calculado a partir do salário bruto, primeiro descontando 11% referente ao INSS, e do resultado, 
 descontando-se 15% de imposto de renda (IR).'''

def calculaSalario():
    renda=float(input("Insira seu salário bruto para descobrir seu salário líquido: "))
    descINSS= renda*0.11
    descIR= (renda-descINSS)*0.15
    salarioliq= renda-(descINSS + descIR)
    print("Foi descontado ", descINSS ,"reais respectivo ao seu INSS e", descIR," reais respectivo ao imposto de renda "
    "com isso o seu salário líquido é: ",salarioliq)
 
calculaSalario()
