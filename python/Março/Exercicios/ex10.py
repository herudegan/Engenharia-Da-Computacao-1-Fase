preco_original = float(input("Digite o preço original do produto: "))

print("Preço original R$ {:.2f} \n"
      "Valor do desconto R$ {:.2f} \n"
      "Preço final R$ {:.2f}".format(preco_original,
                                     preco_original*0.20,
                                     preco_original*0.80))