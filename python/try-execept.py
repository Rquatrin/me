try:
    numero1 = int(input('Digite um número1: '))
    numero2 = int(input('Digite um número2: '))
    print(f'O resultado é: {numero1 / numero2}')

except ZeroDivisionError:
    print('Você não pode dividir um número por zero!')
    
except:
    print('Você precisa digitar um número!')