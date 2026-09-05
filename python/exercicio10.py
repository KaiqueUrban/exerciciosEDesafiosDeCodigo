#Ler um número e verificar se ele é par ou ímpar. 
#Quando for par armazenar esse valor em ‘p’ e quando for ímpar armazená-lo em ‘i’. Exibir ‘i’ e ‘p’ ao final do processamento.

#variáveis
p = 0
i = 0
#entrada
número = int(input("Insira um número "))
#processamento
if número % 2 == 0:
	p = número
else:
	i = número
#saída
print (p)
print (i)