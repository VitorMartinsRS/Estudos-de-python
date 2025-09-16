txt= 'Ana Maria'
interador= iter(txt)  

while True:
    try:
        letra= next(interador)
        print(letra)
    except StopIteration:
        print('FIM')
        break
    # substuido pelo for 
