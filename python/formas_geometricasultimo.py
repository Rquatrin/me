from math import pi

class FormaGeometrica:
    
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
    def metodo_geral(self):
        print('Eu sou uma forma geométrica')
    
class Triangulo(FormaGeometrica):
    
    base = None
    altura = None
    
    def __str__(self):
        return(f'Eu sou um triangulo e minha base é: {self.base} e minha altura é: {self.altura}')
    
    def calcular_area(self):
        return(self.base * self.altura)/2
        
class Quadrilatero(FormaGeometrica):
    
    altura = None
    base = None
    
    def __str__(self):
        return(f'Eu sou um quadrado e minha base é: {self.base} e minha altura é: {self.altura}')
    
    def calcular_area(self):
        return self.base * self.altura
        
class Circulo(FormaGeometrica):   
    
    raio = None
    
    def __str__(self):
        return(f'Eu sou um círculo e meu raio é: {self.raio}')
    
    def calcular_area(self):
        return (self.raio**2) * pi







