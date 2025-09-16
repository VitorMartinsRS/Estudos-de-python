p_secreta = 'ana'
letras_acertadas = []
tentativas = 0
LIMITE_TENTATIVAS = 5

print('-'*40)
print('Bem-vindo ao Jogo da Forca!')
print('-'*40)

while tentativas < LIMITE_TENTATIVAS:
    print(f'Você tem {LIMITE_TENTATIVAS - tentativas} tentativas restantes.')
    
    
    palavra_exibicao = ''
    for letra in p_secreta:
        if letra in letras_acertadas:
            palavra_exibicao += letra
        else:
            palavra_exibicao += '_'
            
    print(f'Palavra: {palavra_exibicao}\n')

    if palavra_exibicao == p_secreta:
        print('Parabéns! Você adivinhou a palavra secreta!')
        break

    letra = input("Informe uma letra para adivinhar: ").lower().strip()
    if letra ==' ':
        if len(letra) != 1 or not letra.isalpha():
            print('Entrada inválida. Por favor, digite apenas uma letra.\n')
            continue
        continue
    if letra in letras_acertadas:
        print('Você já tentou esta letra. Tente outra.\n')
        continue
        
    letras_acertadas.append(letra)

    if letra in p_secreta:
        print('Certo! A letra está na palavra.\n')
    else:
        print('Ops! A letra não está na palavra.\n')
        tentativas += 1
        
if tentativas >= LIMITE_TENTATIVAS:
    print('Suas tentativas acabaram! Você perdeu.')
    print(f'A palavra secreta era: {p_secreta}')