jogadores = []

jogador_1 = {'Nome':'Matheus','pontuação': 0}
jogador_2 = {'Nome':'Leandro','pontuação': 0}

jogadores.append(jogador_1)
jogadores.append(jogador_2)

jogadores[0]['pontuação'] = 10

#print(jogadores[0].get('Nome'))

for jogador in jogadores:
    print('jogador:', jogador.get('Nome'), 'pontuação:', jogador.get('pontuação'))