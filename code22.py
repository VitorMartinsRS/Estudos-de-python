lista= [123, True, 'Vitor Martins', 1.2, []]
print(lista[2]) 
listass= [10,20,30,40]
listass[2]=300
print(listass[2])
listass.append(50)
print(listass)
listass.pop(2)
print(listass,listass.pop() )
listass.clear()
print(listass)
listass.insert(0, 5)
print(listass)
lista_a=[1,2,3,4]
lista_b=[5,6,7,8]
print(lista_a)
print(lista_b)
lista_c=lista_a+lista_b
print(lista_c)
# lista_d=lista_a.extend(lista_b)
# print(lista_d)
lista_a.extend(lista_b)
print(lista_a)