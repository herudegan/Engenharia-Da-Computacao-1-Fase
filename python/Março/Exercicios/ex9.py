valor_combustivel = 4.95
km_por_litro = 20

dinheiro = float(input("Digite o valor que você planeja usar para abastecer: "))

litros = dinheiro/valor_combustivel
distancia = litros*km_por_litro

print("Você poderá comprar {:.2f} litros e percorrer {:.2f} km".format(litros, distancia))