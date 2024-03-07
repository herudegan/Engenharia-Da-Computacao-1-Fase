import math

raio_1 = float(input("Digite o raio do círculo de fora: "))
raio_2 = float(input("Digite o raio do círculo de dentro: "))

calculo_area_coroa = math.pi * (raio_1**2 - raio_2**2)

print("A área da coroa é: {:.2f}".format(calculo_area_coroa))