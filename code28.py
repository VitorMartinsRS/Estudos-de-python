import os
sala = [['Maria','Helena'],['Elaine'],['Luis','João', 'Eduarda']]
try:
    for i in sala:
        for item in i:
            print(item)
            os.system("clear")
except IndexError:
    print('não tem ninguem')