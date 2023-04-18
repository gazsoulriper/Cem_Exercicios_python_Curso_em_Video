# Escreva um programa que leia um valor em metros e mostre na tela as conversões

print("#### tabela de conversão do metro ####")
valor = float(input("\nDigite um valor em metros: "))

dm = valor / 10
cm = valor / 100
mm = valor / 1000
dam = valor * 10
hm = valor * 100
km = valor * 1000

print(f"Valor em mm.....: {mm:.3f} mm")
print(f"Valor em cm.....: {cm:.2f} cm")
print(f"Valor em dm.....: {dm:.1f} dm")
print(f"Valor em dam....: {dam} dam")
print(f"Valor em hm.....: {hm} hm")
print(f"Valor em km.....: {km} km")
