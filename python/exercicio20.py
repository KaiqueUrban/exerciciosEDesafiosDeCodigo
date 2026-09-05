#Elabore um programa que gera e escreve os números ímpares dos números entre 100 e 200.

#variavel
contador = 100
#processamento
while contador <200:
	contador += 1
	if contador %2 == 0:
		continue
	else:
		print(f"O número {contador} é impar")