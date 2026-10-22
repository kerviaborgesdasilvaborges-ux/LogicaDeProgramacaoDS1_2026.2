"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
contador = 0
soma = 0
for i in range(6):
    numero = float(input("digite um valor:"))
    if numero> 0:
        contador = contador + 1
        soma = soma + numero 
        print(f"quantidade de positivos: {contador}")
if contador > 0:
    media = soma / contador
    print(f"media: {media:.1f}")
else:
    print("nenhum numero positivo foi digitado.")

