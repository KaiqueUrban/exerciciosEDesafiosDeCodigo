#Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: "Múltiplo de 10".

#variavel
contador = 0
#processamento
while contador <100:
	print(f"O valor do contador é: {contador}")
	contador += 1
	if contador %10 == 0:
		print(f"{contador} é multiplo de 10")