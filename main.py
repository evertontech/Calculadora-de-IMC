# Calculadora de IMC

#Fórmula do IMC
# IMC = peso (kg) / (altura (m) x altura (m)). 

print("Olá, gostaria de calcular o seu IMC?")

peso = float(input("Informe seu peso: "))

altura = float(input("Informa a sua altura: "))

IMC = peso / (altura * altura)

print("O seu IMC é: {:.2f}".format(IMC))

# Classificação do IMC (adultos)
# Abaixo do peso: abaixo de 18,5
# Peso normal: entre 18,5 e 24,9
# Sobrepeso: entre 25 e 29,9
# Obesidade Grau I: entre 30 e 34,9
# Obesidade Grau II: entre 35 e 39,9
# Obesidade Grau III: acima de 40 

if IMC >= 40:
    print("Obesidade Grau III")
elif IMC > 34.9 and IMC <= 39.9:
    print("Obesidade Grau II")
elif IMC > 29.9 and IMC <= 34.9:
    print("Obesidade Grau I")
elif IMC > 24.9 and IMC <= 29.9:
    print("Sobrepeso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso normal")
else:
    print("Abaixo do peso")
