#Faça um programa que leia 4 nomes e sorteie apenas um nome

import random

alunos = []
aluno1 = input("Digite o nome do primeiro aluno: ")
alunos.append(aluno1)
aluno2 = input("Digite o nome do segundo aluno: ")
alunos.append(aluno2)
aluno3 = input("Digite o nome do terceiro aluno: ")
alunos.append(aluno3)
aluno4 = input("Digite o nome do terceiro aluno: ")
alunos.append(aluno4)
escolhido = random.choice(alunos)

print(f"O aluno escolhido foi: {escolhido}")
