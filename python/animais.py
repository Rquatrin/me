class Cachorro:
    
    nome = None
    raca = None
    tamanho = None
    pelo = None
    status = 'ACORDADO'
    
    def escrever_quem_sou(self):
        print(f'Olá eu sou {self.nome} da raça {self.raca} e meu tamanho é: {self.tamanho.title()}.{status}')
    
    def dormir(self):
        if self.status == 'ACORDADO':
            self.status = 'DORMINDO'
            print('Agora estou ZzZzzzzzzzzzzZZZ')
        
        else:
            print('ZzZzzzzzzzzzzZZZ')
            
    def acordar(self):
        if self.status == 'DORMINDO':
            self.status = 'ACORDADO'
            print('Agora estou acordado')
        
        else:
            print('Estou acordado')
    
    def comer(self):
        if self.status == 'ACORDADO':
            print('Estou comendo')
        
        else:
            print('Estou dormindo, preciso estar acordado para me alimentar')
            
    def correr(self):
        if self.status == 'ACORDADO':
            print('Agora eu vou correr *-*')
        
        else: 
            print('Preciso estar acordado para correr!')
        
    def latir(self):
        if self.status == 'ACORDADO':
            print('Estou latindo')
            
        else:
            ('Não posso latir enquanto estou dormindo')
