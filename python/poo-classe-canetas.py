from time import sleep 
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

print(caneta_a.cor)
print(caneta_a.modelo)
print(caneta_a.qtd_tinta)

for i in range(0,12):

    caneta_a.riscar()
    print(f'Quantidade de tinta: {caneta_a.qtd_tinta}')
    sleep(3)
