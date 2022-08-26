try:
    numero = int(input('Digite um valor entre 10 e 20: '))
    if numero < 10 or numero > 20:
        raise Exception('Número digitado fora da selação!')
    print(f'O dobro do numero {numero} é {numero * 2}')
    
except Exception as e:
    print (e)