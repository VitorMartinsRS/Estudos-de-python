frase = 'eu amo o Sport Club do Recife'
lista_frase = frase.split()
lista=[]
print(lista_frase)
for i, frase in enumerate(lista_frase):
    lista.append(lista_frase[i].lstrip())
    print(lista)
frases_unidas= ' '.join(lista)
print(frases_unidas)