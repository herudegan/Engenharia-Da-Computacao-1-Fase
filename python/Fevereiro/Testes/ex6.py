vf = float(input("Digite o valor final do investimento: "))
meses = int(input("Digite a quantidade de meses: "))
rentabilidade = float(input("Digite a rentabilidade mensal: "))

fv = vf / ((1 + (rentabilidade/100)) ** meses)

print("O valor inicial do investimento é igual a: {:.2f}".format(fv))