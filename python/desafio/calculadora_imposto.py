print('=====| Calculadora de imposto |======\n\n')

nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o valor do produto:(R$) '))
taxa_imposto = float(input('Digite o valor do imposto:(%)'))

valor_imposto = preco_produto * taxa_imposto/100
valor_final = preco_produto + valor_imposto

print(f'O valor do produto: {nome_produto}, é de R${preco_produto}. Com a taxa de {taxa_imposto}% o valor do imposto fica R${valor_imposto} e o VALOR TOTAL: R${valor_final}')
