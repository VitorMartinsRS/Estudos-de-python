nome= input('Informe o nome: ')
tamanho= len(nome)
novo_nome=''
ind=0
while ind <len(nome):
    letra= nome[ind]
    novo_nome+=f'*{letra}'
    ind+=1
novo_nome+='*'
print(novo_nome)