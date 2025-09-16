
for i in range(5):
    print('-'*30)
    print(f'Você tem {i} tentativas de 5')
    print('-'*30)
    letra = ''
    try:
        letra=input("Informe a apenas uma letra para adivinhar a palavra secreta secreta: ") 
        letra_new=str(letra)
        
    except:
        print('Letra invalida')
        
