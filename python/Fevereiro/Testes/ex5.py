vi = float(input("Digite o valor inicial do investimento: "))
meses = int(input("Digite a quantidade de meses: "))
rentabilidade = float(input("Digite a rentabilidade mensal: "))

fv = vi * ((1 + (rentabilidade/100)) ** meses)

print("O valor final do investimento é igual a: {:.2f}".format(fv))