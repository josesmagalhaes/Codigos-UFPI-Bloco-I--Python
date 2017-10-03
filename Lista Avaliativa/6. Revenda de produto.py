"""
Um comerciante comprou um produto e deseja revendê-lo com um lucro de 45%
se o valor de compra for menor do que R$ 20,00; caso contrário, o lucro será
de 30%. Entrar com o valor de compra do produto e exibir seu valor de venda.
"""

custo=float(input("Informe o custo do produto:"))
if (custo<20.00):
    venda=custo+(custo*0.45)
    print ("O produto pode ser vendido por: %.2f"%venda)
else:
    venda=custo+(custo*0.3)
    print("O produto pode ser vendido por: %.2f" % venda)