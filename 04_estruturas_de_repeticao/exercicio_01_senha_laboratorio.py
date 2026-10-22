"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

# TODO: Desenvolva o algoritmo abaixo
senha_correta = "2002"
senha=input ("digite a senha:")
while senha != senha_correta:
    print("senha_invalida:")
    senha = input("digite a senha:")
print("acesso_permitido:")
