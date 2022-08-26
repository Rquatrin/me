from bovinos_lista import bovinos

vacina_a = []
vacina_b = []

for bovino in bovinos:
    
    peso_kg = bovino.get('peso_kg')

    if peso_kg >= 300:
       vacina_a.append(bovino)
    else:
       vacina_b.append(bovino)
    
print('Vacina A: \n')    
for bovino in vacina_a:    
    print(f"{bovino.get('tipo')} {bovino.get('peso_kg')}kg")
print('Vacina B: ')    
for bovino in vacina_b:    
    print(f"{bovino.get('tipo')} {bovino.get('peso_kg')}kg")
    
