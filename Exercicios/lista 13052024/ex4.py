atletas = {}

n = int(input("Digite o número de atletas: "))

for i in range(n):
    nome = input("Digite o nome do atleta: ")
    esporte = input("Digite o esporte do atleta: ")
    atletas[nome] = esporte

def procurar_atleta():
    nome = input("Digite o nome do atleta: ")
    if nome in atletas:
        print("Atleta encontrado na posição",list(atletas).index(nome))
    else:
        print("Atleta não encontrado")

def listar_atletas():
    for nome in atletas:
        print(nome, "-", atletas[nome])

def deletar_atleta():
    nome = input("Digite o nome do atleta: ")
    if nome in atletas:
        del atletas[nome]
        print("Atleta deletado")
    else:
        print("Atleta não encontrado")

def adicionar_atleta():
    nome = input("Digite o nome do atleta: ")
    esporte = input("Digite o esporte do atleta: ")
    atletas[nome] = esporte
    print("Atleta adicionado")



while True:
    escolha = int(input("1 - Procurar atleta"
                        "\n2 - Listar atletas"
                        "\n3 - Deletar atleta"
                        "\n4 - Adicionar atleta"
                        "\n5 - Sair"
                        "\nEscolha: "))
    
    if escolha == 1:
        procurar_atleta()
    elif escolha == 2:
        listar_atletas()
    elif escolha == 3:
        deletar_atleta()
    elif escolha == 4:
        adicionar_atleta()
    elif escolha == 5:
        break