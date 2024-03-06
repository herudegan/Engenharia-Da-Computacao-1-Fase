nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nota = input("Digite sua expectativa de nota: ") # 22 bonoro
regular = input("Você é um aluno regular? (S/N): ")

if regular.capitalize() == "S":
    regular = "Sim"
elif regular.capitalize() == "N":
    regular = "Não"

print("Nome: {}, Idade: {}, Nota: {}, Regular: {}".format(nome, idade, nota, regular))