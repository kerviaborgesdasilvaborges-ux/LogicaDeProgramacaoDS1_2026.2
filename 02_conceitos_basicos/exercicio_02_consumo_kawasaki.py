"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia = float(input(" digite a distancia pecorrida (Km): "))
combustivel = float(input("digite o total de combustivel gasto (Litros):"))
consumo = distancia / combustivel
print(f"consumo medio: {consumo:.2f} km/ l")