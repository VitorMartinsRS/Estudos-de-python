frase ='python.é.aaaaaaaaaaaaaaaaaaaaa.uma.linguagem.de.programação' 'multiparadigma' 'python.foi.criado.por.Guido.Van.Rossum'
#.upper()
#.lower()
#print(frase.count('o'))

i=0
letra_top_um=''
qdt_vezes= 0
while i < len(frase):
    l_a=frase[i]
    
    if l_a =='.':
        i+=1
        continue
    qdt_vez_l_ap=frase.count(l_a)
    if qdt_vezes< qdt_vez_l_ap :
        qdt_vezes=qdt_vez_l_ap
        letra_top_um = l_a

    i+=1
print('a campeã é:', letra_top_um ,'com ',qdt_vez_l_ap,' vezes' )