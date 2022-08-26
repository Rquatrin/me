class caneta:
    cor = None
    modelo = None           #no python não preciso declarar essa parte(cor,modelo,qtd_tinta)
    qtd_tinta = 10
    
    def __init__(self, cor = None, modelo = None):
        self.cor = cor
        self.modelo = modelo
        self.qtd_tinta = 10
    
    def riscar(self):
        
        if self.qtd_tinta:
            print('Estou riscando')
            self.qtd_tinta -= 1
        
        else:
            print('Não posso riscar, estou sem tinta!')

caneta_a = caneta(cor = 'vermelha', modelo = 'quadro branco')
print(caneta_a.cor)
print(caneta_a.modelo)
caneta_a.riscar()
print(caneta_a.qtd_tinta)
