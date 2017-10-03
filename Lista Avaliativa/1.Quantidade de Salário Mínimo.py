"""
Dados os valores do salário mínimo e o salário de uma pessoa,
exibir quantos salários mínimos essa pessoa ganha.
"""

salario_minimo=float(input("Digite o valor do Salário Mínimo: "))
salario_servidor=float(input("Digite o salário do servidor: "))

qtd_salarios=salario_servidor/salario_minimo

print ("A quantidade de salarios que o servidor ganha e: %.2f"% qtd_salarios)