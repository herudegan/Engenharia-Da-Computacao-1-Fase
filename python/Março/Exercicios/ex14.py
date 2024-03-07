peso = float(input('Digite o seu peso (Em kg): '))
altura = float(input('Digite a sua altura (Em M): '))

imc = peso / (altura**2)

print('O seu IMC é: {:.2f}'.format(imc))