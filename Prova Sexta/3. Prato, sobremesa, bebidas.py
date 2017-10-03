"""
Faça um algoritmo que informe a quantidade total de calorias de uma refeição
a partir da escolha do usuário que deverá informar o prato, a sobremesa e a
bebida, conforme a tabelaaseguir:

PRATO                     SOBREMESA                       BEBIDA
Vegetariano:180cal        Abacaxi:75cal                   Chá:20cal
Peixe:230cal              Sorvetediet: 110cal             Sucode laranja:70cal
Frango:250cal             Moussediet:170cal               Sucode melão:100cal
Carne:350cal              Moussede chocolate:200cal       Refrigerantediet:65cal
"""

prato=str(input())
if (prato=='v'):
    p=int(180)
elif (prato=='p'):
    p=int(230)
elif (prato=='f'):
    p=int(250)
elif (prato=='c'):
    p=int(350)

sobremesa=str(input())
if (sobremesa=='a'):
    s=int(75)
elif (sobremesa=='s'):
    s=int(110)
elif (sobremesa=='m'):
    s=int(170)
elif (sobremesa=='c'):
    s=int(200)

bebida=str(input())
if (bebida=='c'):
    b=int(20)
elif(bebida=='l'):
    b=int(70)
elif (bebida=='m'):
    b=int(100)
elif (bebida=='r'):
    b=int(170)

total=p+s+b
print ("O total de calorias consumidas foi: %d"%total)