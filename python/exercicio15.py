#Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se ele é positivo ou negativo.

#entradas
numero = int(input("insira um número: "))
#processamento
if numero %2 == 0:
    if numero > 0:
        print(f"O número inserido é par e positivo")
    else:
        print(f"O número inserido é par e negativo")
else:
    if numero > 0:
        print(f"O número inserido é impar e positivo")
    else:
        print(f"O número inserido é impar e negativo")