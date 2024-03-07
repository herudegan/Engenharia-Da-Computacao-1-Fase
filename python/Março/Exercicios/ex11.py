preco_original = float(input("Digite o preço original do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

print("Preço original R$ {:.2f} \n"
      "Valor do desconto R$ {:.2f} \n"
      "Preço final R$ {:.2f}".format(preco_original, 
                                     preco_original*porcentagem_desconto/100, 
                                     preco_original*(1-porcentagem_desconto/100)))