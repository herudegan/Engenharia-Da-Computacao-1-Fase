a = int(input("Digite um valor: "))
b = int(input("Digite outro valor qualquer diferente de 0: "))

try:
    print(a/b)
except ZeroDivisionError:
    print("O segundo valor não pode ser 0")