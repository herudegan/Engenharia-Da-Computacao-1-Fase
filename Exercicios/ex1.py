lista_pessoas = []

while True:
  nome = input("Digite o nome da pessoa (Ou digite '0' para encerrar): ")
  if nome == '0':
    break

  idade = int(input("Digite a idade da pessoa: "))
  cidade = input("Digite a cidade da pessoa: ")

  pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
  lista_pessoas.append(pessoa)

  print("Pessoa cadastrada com sucesso!")
  print(lista_pessoas)