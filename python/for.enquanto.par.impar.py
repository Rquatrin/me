
lista = range(0,11)

for item in lista:
    resto = item % 2
    if resto == 0:
        print('O número ',item,'é par')
    
    else:
        print('O número ', item,'é ímpar')
    
print('Eu terminei a lista')