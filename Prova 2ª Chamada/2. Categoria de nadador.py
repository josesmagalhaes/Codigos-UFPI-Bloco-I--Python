"""
Faça um programa que receba a idade de um nadador e mostre sua categoria,
 usando as regras a seguir. Para idade inferior a 5, o programa deverá
mostrar uma mensagem de erro.

Categoria                    Idade
Infantil                     5 a 7
Infanto-Juvenil              8 a 10
Juvenil                      11 a 15
Adulto                       16 a 30
Master                       Acima de 30

"""
idade=int(input("Digite a idade do participante: "))
if (idade<5):
    print ("Erro! Idade não permitida!")
elif ((idade>=5)and(idade<=7)):
    print ("Categoria: Infantil")
elif ((idade>=8)and(idade<=10)):
    print ("Categoria: Infanto-Juvenil")
elif ((idade>=11)and(idade<=15)):
    print ("Categoria: Juvenil")
elif ((idade>=16)and(idade<=30)):
    print ("Categoria: Adulto")
elif (idade >30):
    print ("Categoria: Master")

