quilometragem_inicial = float(input("Digite a quilometragem inicial do carro: "))
quilometragem_atual = float(input("Digite a quilometragem atual do carro: "))
quantidade_dias = int(input("Digite a quantos dias você está com esse carro: "))

km_rodados = quilometragem_atual - quilometragem_inicial

custo_dias = 160*quantidade_dias
custo_km = 0.8*km_rodados
custo_total = custo_dias + custo_km

print(f"Km rodados: {km_rodados:.2f}. Custo dias: {custo_dias:.2f}." 
      f" Custo KM: {custo_km:.2f}. Custo Total: {custo_total:.2f}")