
#nota1 = (input("Digite a primeira nota a ser inserida?"))
#nota3 = (input("Digite a terceira nota a ser inserida?"))
#nota2 = (input("Digite a segunda nota a ser inserida?"))

#media = nota1 + nota2 + nota3 / 3

#if (media >=7):
#    print("APROVADO")
#
#elif(media >= 5) and (media< 7):
#    print("RECUPERAÇÃO")
#
#else:
#    print("REPROVADO")
#

valor = 50
 
print(valor)

if valor <= 1830.29:
    valor -= valor * 0.08
    print("desconto aplicado de 0.08")
    print()
elif valor <= 3050.52:
    print("desconto aplicado de 0.09")
    valor -= valor * 0.09
elif valor <= 6101.06:
    print("desconto aplicado de 0.11")
    valor -= valor * 0.11



def calcular_desconto(valor):
 
if valor <= 100:
    valor -= valor * 0.03

elif valor <= 500:
    valor -= valor * 0.10

elif valor <= 1000:
    valor -= valor * 0.20

return valor


