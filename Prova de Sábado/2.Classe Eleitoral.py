"""
Fazer um algoritmo que informe a classe eleitoral de uma pessoa
conforme a tabela abaixo.O usuário deve fornecer a idade da pessoa.

Idade                                       Classe Eleitoral
abaixo de 16 anos                           nãoeleitor
entre 18 e 65 anos                          eleitorobrigatório
entre 16 e 18 anos ou maior que 65 ano      eleitor facultativo
"""

idade=int(input("Digite a idade do indivíduo: "))
if (idade<16):
    print("Não eleitor!")
elif ((idade>=18)and(idade<=65)):
    print("Eleitor Obrigatório!")
else:
    print ("Eleitor Facultativo!")