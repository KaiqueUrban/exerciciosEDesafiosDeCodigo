#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58

#entrada
altura = float(input("Digite sua altura: "))
#processamento
peso_ideal = (72 * altura) - 58
#saída
print(f"O seu peso ideal é de {peso_ideal:.2f} Kg")