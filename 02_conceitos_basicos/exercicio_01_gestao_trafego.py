"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
from os import cpu_count


investimento = float(input("digite o valor total investido  R$:" ))
cliques = float(input("digite o valor total de cliques obtidos R$:"))
cpc = investimento / cliques
print("O CPC medio da campanha é:",cpc)
