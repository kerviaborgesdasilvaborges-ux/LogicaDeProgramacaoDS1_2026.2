"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
consumido = float(input("digite o valor total consumido (em R$:)"))
taxa_serviço = consumido  * 0.10
valor_final_conta = consumido + taxa_serviço
print(f"o valor final da conta a pagar e: r$ {valor_final_conta}:.2f")


