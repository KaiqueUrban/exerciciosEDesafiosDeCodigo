#Elabore um algoritmo que leia um número. Se positivo armazene-o em ‘a’, se for negativo armazene-o em ‘b’. No final mostrar o resultado.

#entrada
num = int(input("Insira um número: "))
#processamento
if num >= 0:
	a = num
	print (f"O número {num} é positivo")
else:
	b = num
	print (f"O número {num} é negativo")