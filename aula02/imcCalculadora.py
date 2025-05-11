def calcular_imc(peso, altura):
    return peso / (altura ** 2)

altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = calcular_imc(peso, altura)

print("Seu IMC é " + "{:.2f}".format(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Acima do Peso")
