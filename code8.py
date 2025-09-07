numstr = input("coloque um numero que vc queira dobrar: ")
try:
    numflot = float(numstr)
    print(f'O dobro de {numstr} é {numflot * 2:.2f}')
except ValueError:
    print("isso não é um numero")