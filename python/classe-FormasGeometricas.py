class FormaGeometrica:
    
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
class Triangulo(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
       return(self.base * self.altura)/2
    
triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'Preto'
triangulo_a.cor_borda = 'Vermelho'
triangulo_a.espessura_borda = 3
triangulo_a.base = 5
triangulo_a.altura = 20

print(triangulo_a.cor_fundo)
print(triangulo_a.calcular_area())

class Quadrilatero(FormaGeometrica):
    
    def calcular_area(self):
        return self.base * self.altura
        
quadrado = Quadrilatero()
quadrado.cor_fundo = 'Vermelho'
quadrado.cor_borda = 'Preto'
quadrado.espessura_borda = 6
quadrado.base = 5
quadrado.altura = 5

print('A área do quadrado é: ',quadrado.calcular_area())