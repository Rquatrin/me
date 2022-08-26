print('Calculadora IMC')

nome = input('Nome: ')
peso = int(input('Peso: kg'))
altura = float(input('Altura: m'))
imc = ''
imc_calculo =round(peso/altura**2,1)

if imc_calculo < 18.5:
    baixo = 'Abaixo do peso'
    imc = baixo

elif imc_calculo > 18.5 and imc_calculo < 24.9:
    p_normal = 'Peso normal'
    imc = p_normal
    
elif imc_calculo > 24.9 and imc_calculo < 29.9:
    sobrepeso = 'Sobrepeso'
    imc_calculo = sobrepeso

elif imc_calculo > 24.9 and imc_calculo < 29.99:
    obesidade_1 = 'Obesidade grau 1'
    imc = obesidade_1
    
elif imc_calculo > 35 and imc_calculo < 39.9:
    obesidade_2 = 'Obesidade grau 2'
    imc = obesidade_2

else:
    obesidade_3 = 'Obesidade grau 3 ou mórbida'
    imc = obesidade_3
    
print(f'O usuário {nome}, com altura de {altura}m e peso de {peso}kg, tem um IMC de {imc_calculo}, classificado como: {imc}')