
lista=[]
lista_enum=enumerate(lista)
lista_enum=list(enumerate(lista))
while True:
    lista_enum=enumerate(lista)
    lista_enum=list(enumerate(lista))
    for i , n in lista_enum:
        print( i , n)

    inpt=input('[i]nserir [a]pagar [l]istar [s]air: ')
    if inpt == 'i':
        item=input('O que deseja adicionar: ')
        lista.append(item)
    elif inpt=='a':
        a=input('Informe o indice do intem que dejesa apagar: ')
        try:
            a = int(a)
            if a <0 or a>len(lista):
                print('Não foi possivel apagar esse item')
            else:
                lista.pop(a)
            print('Item apagado')
        except IndexError:
            print('Informe apenas o indice do produto existente!!!')
        except ValueError:
            print('Informe apenas o indice(ou seja: numeros inteiros)!!!')
        except:
             print('Erro não identificado')
    elif inpt=='l':
        if len(lista) == 0:
            print('Não à itens')
        else:
           continue
    elif inpt =='s':
        print('Lista concluida')
        break
    else:
        print('Comando não indentificado!!!')
        continue
        
    