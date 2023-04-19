# Escreva um programa que pergunte a quantidade de km rodados por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço, sabendo que o carro
# custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print("##### Calculadora de aluguel do carro #####\n")

km_rodados = float(input("Digite a quantidade de quilometros percorridos: "))
qntde_dias = int(input("Quantidade de dias alugado: "))

total_km_rodado = km_rodados * 0.15

total_diaria_aluguel = qntde_dias * 60

valor_total_aluguel = total_km_rodado + total_diaria_aluguel

print(f"O valor total a pagar é de R$ {valor_total_aluguel:.2f}")
