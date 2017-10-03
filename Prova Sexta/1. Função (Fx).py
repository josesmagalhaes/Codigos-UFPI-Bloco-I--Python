"""
Faça um algoritmo que para uma função genérica f(x) = e dados
os valores dos coeficientes a, b e c e um valor para x, exibir o valor de f(x).
"""
print ("Digite um valor para A, B e C respectivamente: ")
a=float(input())
b=float(input())
c=float(input())
x=float(input("Digite um valor para X: "))

fx=a*x*x+b*x+c

print ("O valor da Função F(x) e: %.2f"%fx)