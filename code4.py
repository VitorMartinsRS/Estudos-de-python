
nome = input("Qual é o seu nome? ")
enco = input("O que deseja encontrar? ")

if enco in nome:
    print(f"Item encotredo. '{enco}' está em '{nome}'")
else:
    print(f"Item não encontrado. '{enco}' não está em '{nome}'")