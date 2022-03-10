nota1 = float(input("Digite a primeira nota a ser inserida?"))
nota3 = float(input("Digite a terceira nota a ser inserida?"))
nota2 = float(input("Digite a segunda nota a ser inserida?"))

media = nota1 + nota2 + nota3 / 3

if (media >=7):
    print("APROVADO")

elif(media >= 5) and (media< 7):
    print("RECUPERAÇÃO")

else:
    print("REPROVADO")

    
