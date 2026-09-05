#entradas
codigo_peca = (input("Insira o código da peça: "))
valor_peca = float(input("Insira o valor da peça: "))
quantidade_peca = int(input("Insira a quantidade de peças: "))
#processamento
valor_total = (valor_peca * quantidade_peca)
if valor_total >= 100:
    desconto = float(valor_total * 0.05)
    valor_total = float(valor_total - desconto)
    print("Você recebeu 5% de desconto")
    print(f"Valor Total com Desconto: {valor_total}")
else:
    desconto = (0)
#saida
print("Peça: {0}, Valor total: {1}" .format(codigo_peca, valor_total))