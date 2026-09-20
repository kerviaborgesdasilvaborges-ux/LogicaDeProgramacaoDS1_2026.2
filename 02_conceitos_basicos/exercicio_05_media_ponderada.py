"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("digite a primeira nota da avaliação:"))
nota2 = float(input("digite a segunda nota da avaliação:"))
nota3 = float(input("digite a terceira nota da avaliação:"))
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
print = ("a media final ponderada e:",media)