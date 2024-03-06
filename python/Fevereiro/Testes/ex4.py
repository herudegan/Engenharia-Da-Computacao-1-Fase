n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print("A média das notas é igual a: {}".format(media))

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")