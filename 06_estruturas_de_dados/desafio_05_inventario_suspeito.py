"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
itens = {"mouse","teclado","monitor","teclado","mouse"}
itens_unicos = set(itens)
laboratorio = { 
"mouse" :10,
"teclado" :5,
"monitor" :6,
}
print = ("itens_unicos:" ,itens_unicos)
print = ("quantidade_de_impresorras:",laboratorio.get("impressora",0)) 
