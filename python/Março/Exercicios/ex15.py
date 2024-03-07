import math

raio_hexagono = float(input("Digite o raio do hexágono: "))

angulo_radianos = math.radians(30)

lado_hexagono = 2 * raio_hexagono * math.sin(angulo_radianos)
area_hexagono = (3 * math.sqrt(3) / 2) * lado_hexagono**2

print("A área do hexágono é: {:.2f}, lado igual a {:.2f}".format(area_hexagono, lado_hexagono))