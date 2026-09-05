#Elabore um algoritmo que leia as variáveis ‘c’ e ‘n’, respectivamente código e número de horas trabalhadas de um operário. 
#Calcule o salário sabendo-se que ele ganha R$10,00 por hora. Quando o número de horas exceder a 50, calcule o excesso de pagamento armazenando-o na variável ‘e’. 
#Caso contrário zerar tal variável. A hora excedente de trabalho vale R$20,00.
#No final do processamento, imprimir o salário total e o salário excedente.

#entradas
c = (input("Insira seu código: "))
n = float(input("Insira a quantidade de horas: "))
e = 0
#processamento
if n <= 50:
	salario = float(n * 10)
	print(f"O salário total será de: R${salario:.2f}")
	e = (0)
else:
	excesso_de_horas = float(n - 50)
	e = float(excesso_de_horas * 20)
	salario1 = float(50 * 10)
	salario_total = float(salario1 + e)
	print(f"O salário total será de: R${salario_total:.2f}\nCom um salário excedente de: R${e:.2f}")