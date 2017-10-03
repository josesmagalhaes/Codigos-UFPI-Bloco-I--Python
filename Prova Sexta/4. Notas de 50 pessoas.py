"""
Fazerumalgoritmoque permitaaousuáriodigitarasnotas de50 pessoas.
Apósos números seremdigitados,oprogramadeveexibiramaior nota.
"""

i=0
maior=0
for i in range (0,50):
    notas=float(input("Digite uma nota: "))
    if (notas>maior):
        maior=notas
print ("A maior nota e: %.1f"%maior)


