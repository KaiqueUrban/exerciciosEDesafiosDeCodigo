#a. Leia 4 (quatro) números;
#b. Calcule o quadrado de cada um;
#c. Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
#d. Caso contrário, imprima os valores lidos e seus respectivos quadrados.

#entradas
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
num4 = int(input("Insira o quarto número: "))
#processamento
quadrado = (num1 **2, num2 **2, num3 **2, num4 **2)
if num3 **2 >= 1000:
    print(f"{num3}")
else:
    print(f"{quadrado}")