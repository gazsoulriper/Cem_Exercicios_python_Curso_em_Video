variavel = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(variavel)}")
print(f"Só tem espaços? {variavel.isspace()}")
print(f"Só tem números? {variavel.isnumeric()}")
print(f"Só tem letras? {variavel.isalpha()}")
print(f"É alfanumérico? {variavel.isalnum()}")
print(f"É só maiúsculas? {variavel.isupper()}")
print(f"É só minúsculas? {variavel.islower()}")
print(f"Tem maiúsculas e minúsculas? {variavel.istitle()}")