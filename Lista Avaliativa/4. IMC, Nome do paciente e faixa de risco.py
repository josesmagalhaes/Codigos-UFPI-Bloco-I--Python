"""
Um endocrinologista deseja controlar a saúde de seus pacientes e,
para isso, se utiliza do Índice de Massa Corporal (ICM).
Sabendo-se que o IMC é calculado através da seguinte :

fórmula: Onde: peso é dado em Kg; altura é dada em metros.

Criar um algoritmo que apresente o nome do paciente, seu IMC e sua faixa de risco, conforme a seguinte tabela:

IMC                          FAIXA DE RISCO
Abaixo de 20                 Abaixo do peso
A partir de 20 até 25.       Normal
Acima de 25 até 30.          Excesso de peso
Acima de 30até 35.           Obesidade
Acima de 35.                 Obesidade mórbida
"""

nome=str(input("Digite o nome do paciente: "))
peso=float(input("Digite o peso do paciente: "))
altura=float(input("Digite a altura do paciente: "))

mult=altura*altura
imc=peso/mult

if (imc<20.00):
    print ('O paciente',nome,"consta com o IMC de %.2f, portanto, Abaixo do Peso"%imc)
elif ((imc>=20.00)and(imc<=25.00)):
    print('O paciente', nome, "consta com o IMC de %.2f, portanto, Normal" % imc)
elif ((imc>25.00)and(imc<=30.00)):
    print('O paciente', nome, "consta com o IMC de %.2f, portanto, Excesso de peso" % imc)
elif ((imc>30.00)and(imc<=35.00)):
    print('O paciente', nome, "consta com o IMC de %.2f, portanto, Obesidade" % imc)
elif ((imc>35.00)):
    print('O paciente', nome, "consta com o IMC de %.2f, portanto, Obesidade mórbida" % imc)