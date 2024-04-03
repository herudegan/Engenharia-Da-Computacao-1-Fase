data_nascimento = input("Digite a sua data de nascimento (dd/mm/yyyy): ")

list = []
list = data_nascimento.split('/')

idade = 2024 - int(list[2])  # Não lembro a função para pegar o ano em python

if(idade >= 18):
  print("A pessoa poderá retirar a carteira de motorista esse ano")
else:
  print("A pessoa não poderá retirar a carteira de motorista esse ano")