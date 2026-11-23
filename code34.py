from multiprocessing.pool import TERMINATE


lista =[]
TENTATIVA=1
contador= 0 
while contador < TENTATIVA:
    print('---------------------------------------')
    print('Insira apenas um caracter')
    retorno = input('[A]-adicionar [L]-listar [E]-excluir [F]fechar: ')
    print('---------------------------------------')
    if retorno == 'a':
        item=input('Informe o que deseja adicionar: ') 
        lista.append(item)
        len(lista)
    elif retorno == 'L':
            if len(lista) == 0:
                print('Não à itens')
    elif retorno == 'e':
        lista.__delitem__(input('informe o item que deve ser apagado: '))
    elif retorno == 'f':
        contador= contador+2
    else:
        print('Algo deu errado')
        continue