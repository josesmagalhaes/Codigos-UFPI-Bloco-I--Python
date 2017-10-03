"""
Sabendo que 100 quilowatts de energia custam um sétimo do salário mínimo,
fazer um algoritmo que dados a valor do salário mínimo e a quantidade de
quilowatts gastos por uma residência, exibir: valor em de cada quilowatt,
valor da conta de energia e novo valordacontade energiaapósum descontode 10%.
"""

salario_minimo=float(input("Digite o valor do salário mínimo atual: "))
qtd_quilowatts=float(input("Digite a quantidade de quilowatts: "))

valor_quilowatt=salario_minimo/7
valor_conta=qtd_quilowatts*valor_quilowatt
nova_conta=valor_conta+(valor_conta*0.1)

print("O valor de cada Quilowatt é: %.2f"%valor_quilowatt)
print("O valor da conta é: %.2f"%valor_conta)
print ("O valor da nova conta é: %.2f"%nova_conta)