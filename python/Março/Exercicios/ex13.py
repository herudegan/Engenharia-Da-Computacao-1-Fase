import math

diametro = float(input("Digite o diâmetro do cano (Em cm): "))
velo_fluxo = float(input("Digite a velocidade do fluxo (m/s): "))

area = (math.pi * (diametro / 2)**2) / 10000
fluxo_volumetrico = velo_fluxo * area
vazao_por_hora = fluxo_volumetrico * 3600

print("A vazão do cano é: {:.2f}".format(vazao_por_hora), "m³/h")