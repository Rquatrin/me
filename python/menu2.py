def mostrar_menu():
    print('========================| CALCULADORA |=========================')
    print('Escolha a opção desejada: ')
    print('Somar: (1)')
    print('Subtrair: (2)')
    print('Multiplicar: (3)')
    print('Dividir: (4)')
    print('Sair: (5)')
    return int(input('opcao:'))

def capturar_numeros():
    nr_1 = float(input('Informe o primeiro número: '))
    nr_2 = float(input('Informe o segundo número: '))
    return nr_1,nr_2
    