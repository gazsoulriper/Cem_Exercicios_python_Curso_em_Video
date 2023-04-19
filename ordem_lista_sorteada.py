# Faça um programa que leia o nome de 4 alunos e mostre a ordem sorteada

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do terceiro aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
ordem = random.shuffle(alunos)

print(f"A ordem de apresentação será:\n{alunos}")
