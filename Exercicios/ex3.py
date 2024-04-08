from collections import deque

pilha = deque()

text = input("Digite a expressão a qual você quer verificar: \n")

for x in text:
  if(x == "("):
    pilha.append(x)
  elif(x == ")" and len(pilha) >= 1):
    pilha.pop()
  elif(x == ")" and len(pilha) == 0):
    print("Incorreta.")
    exit()

if(len(pilha) >= 1):
  print("Incorreta.")
elif(len(pilha) == 0):
  print("Correta.")
else:
  print("Algo deu errado.")