#João da Silva, pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50Kg) deve pagar uma multa de R$4,00 por Kg excedente. 
#João precisa que você faça um algoritmo que leia a variável ‘p’ (peso de peixes) e verifique se há excesso. 
#Se houver, gravar na variável ‘e’(excesso) e na variável ‘m’ (valor da multa) que João deverá pagar. 
#Caso contrário, mostrar tais variáveis com o conteúdo 0.

#constantes
PESO = 50
MULTA = 4.00
#entrada
peso_do_peixe = float(input("Insira o peso do peixe "))
#processamento
p = peso_do_peixe
if peso_do_peixe > 50:
	excesso = (peso_do_peixe - 50)
	e = excesso
	multa = (excesso * MULTA)
	m = multa
else:
	multa = 0
#saída
print(f"O valor da multa a ser pago é de: R${multa:.2f}")