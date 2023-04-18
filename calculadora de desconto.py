# Escreva um programa que receba o valor do produto ea % do desconto
# e mostre na tela o valor antigo e o novo valor ja aplicado o desconto

print("#### Calculadora de descontos ####\n")

valor_produto = float(input("Digite o valor do produto: R$ "))
desconto = float(input("Digite quantos porcento será dado de desconto: "))

novo_preco = valor_produto - (valor_produto * desconto) / 100

print(
    f"Valor sem desconto...: R$ {valor_produto:.2f}\n"
    f"Valor do desconto....: {desconto} %\n"
    f"Valor com desconto...: R$ {novo_preco:.2f}"
)
