def entrar_inteiro():
    solicitar_inteiro = True
    while solicitar_inteiro:
        try:
            inteiro =  int(input('Digite um número inteiro: '))
            solicitar_inteiro = False
            return inteiro
        
        except:
            solicitar_inteiro = True
            print('Você deve digitar um número inteiro!')
        
numero = entrar_inteiro()

print(f'O dobro de {numero} é {numero * 2}')
