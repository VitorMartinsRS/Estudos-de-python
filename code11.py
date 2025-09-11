entrada = input('What time is it? ')

try:
    hr= int(entrada)
    dia= (hr >= 0) and (hr <= 11) or hr == 24
    tarde= hr >=12 and hr <=17
    noite= hr >=18 and hr <=23

    if dia:
        print('Bom dia')
    elif tarde:
        print("Boa trade")
    elif noite:
        print("Boa noite")
    else:
        print("Essa hora n existe")
except:
    print('caracter não reconhecido')
