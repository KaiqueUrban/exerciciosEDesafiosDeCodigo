#Faça um algoritmo que converta metros para centímetros.

#entradas
metros = float(input("Insira um valor em metros "))
#processamento
conversão1 = metros * 100
conversão2 = metros * 1000
#saída
print(f"{metros} metros equivalem a {conversão1} centímetros \nE {conversão1} centímetros equivalem a {conversão2} milímetros")