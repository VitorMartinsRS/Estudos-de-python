
while True:
    sair= input('Para sair escreva "sair" se nn apenas ignore: ')
    sair=sair.lower()   
    if sair =='sair':
        print('Programa finalizado com sucesso')
        break
    a = 0 
    b = 0
    c = "+-*/"
    try:
        print("Digite o primeiro numero: ")
        a = int(input())    
        print("Digite o segundo numero: ")
        b = int(input())    
        print("Digite a operacao: ")
        c = str(input())
        if c == '+':
            print('Resultado: ', str(a + b))
        elif c == '-':
            print('Resultado: ', str(a - b))
        elif c == '*':
            print('Resultado: ', str(a * b))
        elif c == '/':
            print('Resultado: ', str(a / b))
        else:
            print('Operaçõa invalida')
    except:
        print('ERRO NO PROCESSAMENTO')
        break