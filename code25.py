lista=['Vitor','Ana', 'Maria']
lista.append('João')

lista_enumerada= enumerate(lista)
lista_enumerada = list(enumerate(lista))

print(lista_enumerada)
while True:
    for i , n in lista_enumerada:
        print(i,n)
    b=input()
    if b==0:
        break