
from sqlalchemy import true


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#Esturtura de repetição que exibe a pergunta 
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()
    
    #Esturtura de repetição que exibe as alternativas para cada pergunta 
    opcoes=pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'({i}){opcao}')
        

    #Pede ao usuario para indicar o indice da resposta        
    resposta=input('Escolha a alternativa: ')    

    acerto = False
    resposta_int=None
    #Verifica de ele digitou algo querente
    if resposta.isdigit():
        resposta_int = int(resposta)
        #Verifica se o digito é valido  
        if resposta_int != None and resposta_int>=0 and resposta_int<=3:
            
            #se o digito é valido compara com a resposta
            if opcoes[resposta_int] == pergunta['Resposta']:
                acerto = True
            else:
                print(f'Errou a resposta é {pergunta['Resposta']}')
    if acerto:
        print('Acertou')
   