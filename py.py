def multiplica(*args):
    total= 1 
    for n in args:
        total*=n
    return total
   
argumentos_para_multiplicacao= multiplica(1,2,3)
print(argumentos_para_multiplicacao)