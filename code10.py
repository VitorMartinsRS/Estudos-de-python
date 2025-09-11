entrada = input("Iforme um numero inteiro:")

try :
    num= int(entrada)
    #cauculo 
    resultado = (num % 2)

    par= resultado < 1
    impar = not par

    if par:
        print(f'O numero {num} é par')
    if impar:
        print(f"O numero {num} é impar")
except:
    print(f'A expreção ({entrada}) não é invalido')
