nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))

if(idade >= 0 and idade <= 15):
  print("Você está abaixo da idade permitida")
elif(idade <= 17 and peso > 50):
  print("Você pode doar sangue com a autorização de um pai ou responsável")
elif(idade <= 69 and peso > 50):
  print("Você pode doar sangue")
elif(idade > 69):
  print("Você está acima da idade permitida")
else:
  print("Valores inválidos")