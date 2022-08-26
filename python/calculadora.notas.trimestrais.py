print('==================| Calculadora de notas trimestrais:  |====================')
nota1 = float(input('Digite o valor da primeira nota trimestral: '))
nota2 = float(input('Digite o valor da segunda nota trimestral' ))
nota3 = float(input('Digite o valor da terceira nota trimestral '))

notafinal = (nota1 + nota2 + nota3) / 3

print('A média final é: ',notafinal)

if notafinal >= 6:
    print('O aluno está aprovado com a nota: ',round(notafinal,2))
    
else:
    print('O aluno está reprovado com a nota: ',round(notafinal,2))