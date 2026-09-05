#Faça um algoritmo que determine o maior entre N números.
#A condição de parada é a entrada de um valor 0, ou seja, o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0 (ZERO).

#entrada
numero = int(input("Insira um número: "))
maior = numero
#processamento
while numero > 0:
	numero = int(input("Insira um novo número: "))
	if numero > maior:
		maior = numero
		print(f"{numero}")
		if numero == 0:
			break
	