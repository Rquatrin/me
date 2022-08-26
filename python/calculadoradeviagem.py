print('=====================| Calculadora para hotel |=======================')

valor_hospedagem = float(input('\nDigite o valor da diária para uma pessoa :'))

qtd_pessoas = int(input('Digite a quantidade de pessoas: '))

valortotal_hospedagem = valor_hospedagem * qtd_pessoas

print('\nO valor total para',qtd_pessoas, 'pessoas é: R$',valortotal_hospedagem)

print('\n\n====================| Calculadora para pedágio |=====================')

valor_pedagio = float(input('\nDigite o valor do pedágio: '))

qtd_pedagio = int(input('Digite a quanditade total de pedágio da viagem: '))

valortotal_pedagio = valor_pedagio * qtd_pedagio

print('\nO valor total para',qtd_pedagio,'pedágio(s) é: R$',valortotal_pedagio)

print('\n\n=====================| Calculadora para combustível |=====================')

valor_combustível = float(input('\n\nDigite o valor do combustível selecionado por litro: '))
distancia = float(input('Digite a distancia total que será percorrida na viagem em Km:' ))
autonomia_automovel = float(input('Digite a autonomia do automóvel (km/L): '))

valortotal_combustivel = (distancia / autonomia_automovel) * valor_combustível

print('\nO valor total de combustível para',distancia,'Km, será: R$',valortotal_combustivel)

print('\n\n=====================| Total da viagem |=====================')

valortotal_viagem = valortotal_hospedagem + valortotal_pedagio + valortotal_combustivel

print('O valor total da viagem será: R$',round(valortotal_viagem,2),'\n')
print(80 * '-')


print('\nO valor total para',qtd_pessoas, 'pessoas é: R$',round(valortotal_hospedagem,2))
print('\nO valor total para',qtd_pedagio,'pedágio(s) é: R$',round(valortotal_pedagio,2))
print('valor total da combustível será: R$', round(valortotal_combustivel,2))



