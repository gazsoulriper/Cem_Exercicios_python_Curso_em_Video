## Escreva um programa que receba um número e na sequência mostre
## seu dobro, triplo e raiz quadrada

double = 0
triple = 0
raiz_quadrada = 0

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f"O dobro de {numero} é {dobro}")
print(f"O triplo de {numero} é {triplo}")
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")
