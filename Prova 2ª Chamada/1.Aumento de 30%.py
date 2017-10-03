"""
Uma empresa decide dar um aumento de 30% aos funcionários
com salários inferiores a R$900,00. Faça um programa em que
seja digitado o salário de um funcionário e mostre o valor
do salário reajustado.

"""

salario=float(input("Digite o salário do servidor: "))
if (salario<900.00):
    salario_reajustado=salario+(salario*0.3)
    print ("O valor do salário com reajuste é: %.2f"%salario_reajustado)
else:
    print ("Servidor não tem direito a reajuste!")
