# Escreva um programa que calcule a área de uma parede em metros e o 
# gasto de tinta para pintar toda a parede sabendo que cada litro de tinta 
# pinta uma área de 2m²

print("#### Calculadora de quantidade de tinta para parede ####\n")

altura = float(input("Insira o valor da altura da parede em metros: "))
largura = float(input("Insira o valor da largura da parede em metros: "))

area = altura * largura
qntde_tinta = area/2

print(f"\nA área total da parede é de {area:.2f} metros e será gasto {qntde_tinta:.2f} litros "
            "de tinta para pintar toda a parede.")