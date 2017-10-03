"""
Dados N números digitados pelo usuário, exibir os somatórios deles.
Onde o valor N é dado também pelo usuário.
"""

n=int(input("Digite a quantidade de numeros a serem digitados: "))
i=1
soma=0
for i in range(0,n):
    num=int(input("Digite um número inteiro"))
    soma+=num
print ("A soma dos números digitados e: %d"%soma)