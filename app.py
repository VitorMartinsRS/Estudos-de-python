# perguntas = [
#     {
#         'pergunta':'Quanto é 2+2?',
#         'alternativas':['1', '2', '3', '4'],
#         'resposta':'4'
#     },
#     {
#         'pergunta':'Quanto é 3+2?',
#         'alternativas':['1', '5', '3', '4'],
#         'resposta':'5'
#     },
#     {
#         'pergunta':'Quanto é 6+2?',
#         'alternativas':['8', '2', '3', '4'],
#         'resposta':'8'
#     },
#     {
#         'pergunta':'Quanto é 2*8?',
#         'alternativas':['8', '16', '3', '4'],
#         'resposta':'16'
#     },
#     {
#         'pergunta':'Quanto é 6*2?',
#         'alternativas':['8', '12', '3', '4'],
#         'resposta':'12'
#     }
# ]

# for pergunta in perguntas:
    
#     print(pergunta['pergunta'])
    
#     for i, alternativas in enumerate(pergunta['alternativas']):
        
#         print(f'({i}) {alternativas}')
        
#     qtd_alternativa = len(pergunta['alternativas'])
   
#     resposta=input('Qual a resposta?')
   
#     acerto = False
   
#     resposta_int =None
    
#     if resposta.isdigit():
#         resposta_int=int(resposta)
          
#     if resposta_int != None:
#         if resposta_int <= qtd_alternativa and resposta_int<=0:
#             if  len(pergunta['alternativas']) == perguntas['resposta']:
#                 acerto= True
    
#     if acerto:
#         print('acertou')
#     else:
#         print('errou')    
      # Exercício - sistema de perguntas e respostas


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

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')