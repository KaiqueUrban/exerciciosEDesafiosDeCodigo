#Faça um algoritmo para “Calcular o estoque médio de uma peça”, sendo que: estoque medio = (quantidade minima + quantidade maxima) / 2

#entradas
quantidade_minima = int(input("Insira a quantidade mínima "))
quantidade_maxima = int(input("Insira a quantidade máxima"))
#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#saída
print("O estoque medio é de {0}" .format (estoque_medio))