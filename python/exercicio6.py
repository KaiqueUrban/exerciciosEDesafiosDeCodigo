#Faça um algoritmo que pergunte o quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

#entradas
horas_trabalhadas = int(input("Insira o total de horas trabalhadas: "))
salário_hora = float(input("Insira o valor da sua hora trabalhada: "))
#processamento
salário_mês = horas_trabalhadas * salário_hora
#saída
print(f"O valor total do salario será de R${salário_mês:.2f}")