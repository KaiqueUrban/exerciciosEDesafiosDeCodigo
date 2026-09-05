#A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente.
#O índice de poluição aceitável varia de 0.05 até 0.25.
#Se o índice sobe para 0.3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades.
#Se o índice crescer para 0.4 , as indústrias do 1º e 2º grupos são intimadas a suspenderem suas atividades
#Se o índice atingir 0.5 todos os grupos devem ser notificados a paralisarem suas atividades.
#Faça um algoritmo que leia o índice de poluição medido e emita notificação adequada aos diferentes grupos de empresas.

#entrada
indice = float(input("Insira o indice medido: "))
#processamento
if 0.05 <= indice <= 0.25:
    print("Índice dentro dos limites aceitáveis.")
elif 0.25 < indice < 0.3:
    print("Índice fora do limite, mas sem ação imediata.")
elif 0.3 <= indice < 0.4:
    print("Suspender imediatamente as atividades das empresas que compõem o 1º grupo!")
elif 0.4 <= indice < 0.5:
    print("Suspender imediatamente as atividades das empresas que compõem o 1º e 2º grupos!")
elif indice >= 0.5:
    print("Suspender imediatamente as atividades de todos os grupos de empresas!")
else:
    print("Índice fora dos limites considerados.")