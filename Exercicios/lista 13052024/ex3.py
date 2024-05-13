times = {}

n = int(input("Digite o número de times: "))

for i in range(n):
    nome = input("Digite o nome do time: ")
    times[i] = nome

while True:
    escolha = int(input("1 - Procurar time"
                        "\n2 - Listar times"
                        "\n3 - Deletar time"
                        "\n4 - Adicionar time"
                        "\n5 - Sair"
                        "\nEscolha: "))

    if escolha == 1:
        nome = input("Digite o nome do time: ")
        for i in times:
            if times[i] == nome:
                print("Time encontrado na posição", i)
                break
        else:
            print("Time não encontrado")
    elif escolha == 2:
        for i in times:
            print(times[i])
    elif escolha == 3:
        nome = input("Digite o nome do time: ")
        for i in times:
            if times[i] == nome:
                del times[i]
                print("Time deletado")
                break
        else:
            print("Time não encontrado")
    elif escolha == 4:
        nome = input("Digite o nome do time: ")
        times[n] = nome
        n += 1
        print("Time adicionado")
    elif escolha == 5:
        break
    else:
        print("Opção inválida")