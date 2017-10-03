"""
Fazer um algoritmo que permita ao usuário digitar cada uma das
notas de uma avaliação de 50 alunos de uma turma. Após as notas
serem digitadas, o programa deve exibir o valor da maior nota.

"""
i=1
maior=0
for i in range (0,50):
    nota=float(input("Digite uma nota: "))
    if (nota>maior):
        maior=nota
print ("A maior nota é: %.1f"%maior)