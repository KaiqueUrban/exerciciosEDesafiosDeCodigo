#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7 * altura) - 58
#Para mulheres: (62.1 * altura) - 44.7

#entradas
altura = float(input("Insira sua altura: "))
gênero = input("Você é homem ou mulher? ")
#processamento
if gênero.lower() == "homem":
	peso_ideal = (72 * altura) - 58
elif gênero.lower() == "mulher":
	peso_ideal = (62.1 * altura) - 44.7
else:
	peso_ideal = 0
	print(f"Gênero desconhecido!")
#saída
print("Seu peso ideal é {0:.2f}" .format(peso_ideal))