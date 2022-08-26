class caneta:
    cor = None
    modelo = None
    qtd_tinta = 10
    
    def riscar(self):
        
        if self.qtd_tinta:
            print('Estou riscando')
            self.qtd_tinta -= 1
        
        else:
            print('Não posso riscar, estou sem tinta!')

caneta_a = caneta()
caneta_a.cor = 'vermelha'
caneta_a.modelo = 'caneta quadro branco'

caneta_b = caneta()
caneta_b.cor = 'preta'
caneta_b.modelo = 'caneta quadro branco'

print(caneta_b.cor)
print(caneta_b.modelo)
print('Quantidade de tinta inicial: ',caneta_b.qtd_tinta)
caneta_b.riscar()
print('Quantidade de tinta restante: ',caneta_b.qtd_tinta)







