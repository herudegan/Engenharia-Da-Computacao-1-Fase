series = {}

n = int(input("Digite o número de séries: "))

for i in range(n):
    nome = input("Digite o nome da série: ")
    series[i] = nome

while True:
    escolha = int(input("1 - Procurar série"
                        "\n2 - Listar séries"
                        "\n3 - Deletar série"
                        "\n4 - Adicionar série"
                        "\n5 - Sair"
                        "\nEscolha: "))

    if escolha == 1:
        nome = input("Digite o nome da série: ")
        for i in series:
            if series[i] == nome:
                print("Série encontrada na posição", i)
                break
        else:
            print("Série não encontrada")
    elif escolha == 2:
        for i in series:
            print(series[i])
    elif escolha == 3:
        nome = input("Digite o nome da série: ")
        for i in series:
            if series[i] == nome:
                del series[i]
                print("Série deletada")
                break
        else:
            print("Série não encontrada")
    elif escolha == 4:
        nome = input("Digite o nome da série: ")
        series[n] = nome
        n += 1
        print("Série adicionada")
    elif escolha == 5:
        break
    else:
        print("Opção inválida")