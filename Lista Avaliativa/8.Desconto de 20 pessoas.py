"""
Dados os salários bruto de 20 pessoas, exibir o desconto do INSS para cada pessoa segundo a tabela abaixo:

Salário                                                     Percentual do desconto
Menor ou igual a R$ 600,00                                  Insento
Maior que R$ 600,00 e menor ou igual a R$ 1200,00           20%
Maior que R$ 1200,00 e menor ou igual 2000,00               25%
Maior que R$ 2000,00                                        30%

"""

i=1
for i in range(0,20):
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
