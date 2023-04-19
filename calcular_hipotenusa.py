# Escreva um algoritmo que a pessoa inserindo os catetos, obtenha o valor da hipotenusa

import math

cat_oposto = float(input("Digite o valor do cateto oposto: "))
cat_adjacente = float(input("Digite o valor do cateto adjacente: "))
print(f"A hipotenusa é {math.hypot(cat_oposto, cat_adjacente):.2f}")