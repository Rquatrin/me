from formas_geometricas1 import Triangulo, Quadrilatero, Circulo

formas = []


triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'Preto'
triangulo_a.cor_borda = 'Vermelho'
triangulo_a.espessura_borda = 3
triangulo_a.base = 5
triangulo_a.altura = 20
formas.append(triangulo_a)

quadrado = Quadrilatero()
quadrado.cor_fundo = 'Vermelho'
quadrado.cor_borda = 'Preto'
quadrado.espessura_borda = 6
quadrado.base = 5
quadrado.altura = 5
formas.append(quadrado)

circulo_a = Circulo()
circulo_a.cor_fundo = 'Azul'
circulo_a.cor_borda = 'Branco'
circulo_a.espessura_borda = 2
circulo_a.raio = 6
formas.append(circulo_a)
    

for forma in formas:
    print('área: ',forma.calcular_area())
