capa = 24.95
#desconto = 0.35
# transporte = 3 primeiro exemplar, 0.75 para os demais
# qual o custo total de atacado para x cópias? solicite o valor de x. mostre o custo total da compra
vfc = capa*0.65
nc = int(input("Digite a quantidade de cópias: "))
if(nc == 1):
    print("O custo total da compra é igual a: {:.2f}".format((vfc*nc) + 3))
elif(nc <= 0):
    print("Digite um valor válido")
else:
    print("O custo total da compra é igual a: {:.2f}".format((vfc*nc) + 3 + ((nc-1)*0.75)))

