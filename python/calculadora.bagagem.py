kg_bagagem = float(input('Digite o valor da bagagem(Kg) :'))

if kg_bagagem > 10:
    kg_excedente = kg_bagagem - 10
    valortotal_ex = kg_excedente * 2
    print('O valor do peso (',kg_bagagem,'Kg), excedente(',kg_excedente,'Kg) a ser pago é: R$',valortotal_ex)
    
else:
    print('O peso não foi excedido.')

    