from random import choice

opcoes = ['*', '']

batalha_naval = [
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
	[choice(opcoes), choice(opcoes), choice(opcoes), choice(opcoes)],
]
placar_geral = 0
print('=====| BATALHA NAVAL |=====\n\n')

for jogada in range(1,6):

    linha = int(input('Digite a linha: (1 a 5) \n'))
    coluna = int(input('Digite a coluna: (1 a 4) '))
    

    if linha < 6 and coluna < 5 and batalha_naval[linha-1][coluna-1] == '*':
        placar_geral = placar_geral + 10
        print('Você acertou!\n')
    
    elif linha < 6 and coluna < 5 and batalha_naval[linha-1][coluna-1] == '':
        placar_geral = placar_geral - 10
        print('Você errou!\n')
    
    
print(f'Placar final: {placar_geral}')

