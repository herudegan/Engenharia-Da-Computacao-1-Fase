def inserir_elemento(lista, elemento):
    lista.append(elemento)
    print("Elemento {}, inserido com sucesso!".format(elemento))

def main():
    lista_pessoas = []

    while True:
        print("1 - Inserir pessoa")
        print("0 - Encerrar")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            break
        
        elif opcao == 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            cidade = input("Digite a cidade da pessoa: ")

            pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
            inserir_elemento(lista_pessoas, pessoa)

main()