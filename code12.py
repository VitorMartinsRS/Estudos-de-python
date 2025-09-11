nome= input("what't your fist name: ")
if nome.isalpha():
   
    qdt_letras = len(nome) 
    curto= qdt_letras>=1 and qdt_letras<=4
    medio= qdt_letras>=5 and qdt_letras<=6
    grande= qdt_letras>=7

    if curto:
        print('Your name is small')
    elif medio:
        print('Your name is average')
    elif grande:
        print('Your name is big')
    else:
        print('You did not provide your fist name')
else:
    print("You did not provide your fist name ")