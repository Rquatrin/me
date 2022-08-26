print('=========================| ORÇAMENTO PARA SMARTPHONES |===========================')

nome_cliente = input('\n\nDigite o nome do cliente: ')
modelo_smartphone = input('\nDigite o modelo do smartphone: ')
valor_smartphone = float(input('\nDigite o valor do smartphone: '))
valortotal_smartphone = valor_smartphone + 400

print('\nO valor total do smartphone,',modelo_smartphone,'é: R$',valortotal_smartphone,'.Para o cliente: ',nome_cliente)
