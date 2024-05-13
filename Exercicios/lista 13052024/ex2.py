estados = {}

n = int(input("Digite o número de estados: "))

for i in range(n):
    nome = input("Digite o nome do estado: ")
    capital = input("Digite a capital do estado: ")
    estados[nome] = capital

def procurar_estado():
    nome = input("Digite o nome do estado: ")
    if nome in estados:
        print("Estado encontrado na posição",list(estados).index(nome))
    else:
        print("Estado não encontrado")

def listar_estados():
    for estado in estados:
        print(estado, "-", estados[estado])

def deletar_estado():
    nome = input("Digite o nome do estado: ")
    if nome in estados:
        del estados[nome]
        print("Estado deletado")
    else:
        print("Estado não encontrado")

def adicionar_estado():
    nome = input("Digite o nome do estado: ")
    capital = input("Digite a capital do estado: ")
    estados[nome] = capital
    print("Estado adicionado")



while True:
    escolha = int(input("1 - Procurar estado"
                        "\n2 - Listar estados"
                        "\n3 - Deletar estado"
                        "\n4 - Adicionar estado"
                        "\n5 - Sair"
                        "\nEscolha: "))
    
    if escolha == 1:
        procurar_estado()
    elif escolha == 2:
        listar_estados()
    elif escolha == 3:
        deletar_estado()
    elif escolha == 4:
        adicionar_estado()
    elif escolha == 5:
        break