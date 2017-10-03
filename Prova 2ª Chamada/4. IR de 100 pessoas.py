"""
Dados os salários de 100 pessoas, exibir o imposto de renda
cobrado para cada pessoa de acordo com a tabela abaixo.

Salário                                                     Percentual de Desconto
Menor ou igual a R$ 600,00                                  Isento
Maior que R$ 600,00 e menor ou igual a R$ 1200,00           20%
Maior que R$ 1200,00 e menor ou igual 2000,00               25%
Maior que R$ 2000,00                                        30%

"""
i=1
for i in range (0,3):
    salario=float(input("Digite o salário do servidor: "))
    if (salario<600.00):
        print ("Insento")
    elif ((salario>600.00)and(salario<=1200.00)):
        print ("O desconto do servidor é: %.2f"%desconto)
    elif ((salario>1200.00)and(salario<=2000.00)):
        desconto=salario*0.25
        print ("O descinto o servidor é: %2.f"%desconto)
    elif (salario>3000.00):
        desconto=salario*0.3
        print ("O desconto do servidor é: %f"%desconto)