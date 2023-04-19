import math
print("#### Calcular Seno, Cosseno e Tangente ####\n")
angulo = int(input("Digite o valor do ângulo: "))
print(f"\nSeno do ângulo de {angulo}° é {math.sin(math.radians(angulo)):.2f}\n"
      f"Cosseno do ângulo de {angulo}° é {math.cos(math.radians(angulo)):.2f}\n"
      f"Tangente do ângulo de {angulo}° é {math.tan(math.radians(angulo)):.2f}"
      )

