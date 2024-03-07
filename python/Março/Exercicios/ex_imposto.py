def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input inválido.")

def calculate_deductions(remuneracao, inss, dependentes):
    DEDUCAO = 564.80
    DEDUCAO_DEPENDENTES = 189.59
    deducao_dependentes = dependentes * DEDUCAO_DEPENDENTES
    deducao_tradicional = deducao_dependentes + inss
    valor_base_tradicional = remuneracao - deducao_tradicional
    valor_base = remuneracao - DEDUCAO
    return valor_base_tradicional, valor_base

def calculate_tax(valor_base):
    if valor_base < 2259.20:
        return valor_base
    elif 2259.20 < valor_base <= 2826.65:
        return valor_base * 0.075 - 169.44
    elif 2826.65 < valor_base <= 3751.05:
        # Continue your conditions here
        pass

def main():
    remuneracao = get_user_input("Digite sua renda mensal: ")
    inss = get_user_input("Digite o desconto que tera no INSS: ")
    dependentes = get_user_input("Digite o numero de dependentes: ")
    valor_base_tradicional, valor_base = calculate_deductions(remuneracao, inss, dependentes)
    total = calculate_tax(valor_base)
    print(f"A taxa total é de: {total:.2f}")

if __name__ == "__main__":
    main()