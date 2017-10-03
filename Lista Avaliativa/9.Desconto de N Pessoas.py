"""
Refazer a questão 08, mas o algoritmo deve calcular o salário de N pessoas, sendo que N é dado pelo usuário:

Salário                                                     Percentual do desconto
Menor ou igual a R$ 600,00                                  Insento
Maior que R$ 600,00 e menor ou igual a R$ 1200,00           20%
Maior que R$ 1200,00 e menor ou igual 2000,00               25%
Maior que R$ 2000,00                                        30%

"""

n=int(input("Digite a quantidade de servidores a serem consultados: "))
i=1
for i in range(0,n):
    print("Digite o salário do servidor: ")
    salario = float(input())
    if (salario <= 600.00):
        print("Insento")
    elif ((salario > 600.00) and (salario <= 1200.00)):
        desconto = salario * 0.2
        print("O desconto para o salário fornecido é: %.2f" % desconto)
    elif ((salario > 1200.00) and (salario <= 2000.00)):
        desconto = salario * 0.25
        print("O desconto para o salário fornecido é: %.2f" % desconto)
    elif (salario > 2000.00):
        print("O desconto para o salário fornecido é: %.2f" % desconto)
