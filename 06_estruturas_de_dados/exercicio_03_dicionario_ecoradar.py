"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:

membros = {
    "101": "Professor",
    "102": "Coordenador",
    "103": "Monitor"
}

matricula = input("Digite sua matrícula: ")

print(membros.get(matricula, "Matrícula não encontrada!"))