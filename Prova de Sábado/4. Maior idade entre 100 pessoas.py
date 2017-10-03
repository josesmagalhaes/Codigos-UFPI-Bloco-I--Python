"""
Fazer um algoritmo que permita ao usuário digitar as idades de100 pessoas.
Após os números serem digitados,o programa deve exibir a maior idade digitada.
"""

i=1
idade=0
maior=idade
for i in range (0,100):
    idade=int(input("Digite uma idade: "))
    if(idade>maior):
        maior=idade
print ("A maior idade é: %d"%maior)