turno = input("Digite em qual turno você estuda: \n"
              "M - Matutino. \n"
              "V - Vespertino. \n"
              "N - Noturno. \n")

if (turno.capitalize() == "M"):
  print("Bom Dia!")
elif(turno.capitalize() == "V"):
  print("Boa Tarde!")
elif(turno.capitalize() == "N"):
  print("Boa Noite!")
else:
  print("Valor errado.")