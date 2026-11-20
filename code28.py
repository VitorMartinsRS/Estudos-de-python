import subprocess
sala = [['Maria','Helena'],['Elaine'],['Luis','João', 'Eduarda']]
try:
    for i in sala:
        for item in i:
            print(item)
            subprocess.run(['clear'])
except IndexError:
    print('não tem ninguem')