"""
Dado um número inteiro no formato CDU, exibir o número no formato UDC.
Exemplo: 123, será321. O número deverá ser atribuído a uma variável antes.
deserexibido.
"""
num=int(input("Digite um número inteiro: "))
c=num//100
d=(num % 100)//10
u=(num % 100)% 10

print ('A ordem reversa de',num,'é:',u,d,c,"!")