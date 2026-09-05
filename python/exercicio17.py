#Elabore um algoritmo que dada a idade de um nadador, classifique-o em uma das seguintes categorias:
#Infantil A = 5 a 7 anos
#Infantil B = 8 a 11 anos
#Juvenil A = 12 a 13 anos
#Juvenil B = 14 a 17 anos
#adultos = > de 18 anos

#entrada
idade = int(input("Insira sua idade: "))
#processamento
if 5 <= idade <= 7:
	print("Infantil A")
elif 8 <= idade <= 11:
	print("Infantil B")
elif 12 <= idade <= 13:
	print("Juvenil A")
elif 14<= idade <= 17:
	print("Juvenil B")
else:
	print("Adulto")