from datetime import datetime

class Pessoas:
    
    nome = None
    data_nascimento = None
    fun_profissional = None
    email = None
    telefone = None
    
    def imprimir_cartao_visita(self):
        print()
        
pessoa_1 = Pessoas()
pessoa_1.nome = input('Digite o nome da pessoa: ')
pessoa_1.data_nascimento = datetime.strptime(input('Digite a data de nascimento: DD/MM/AAAA'), '%d/%m/%Y').date()
pessoa_1.fun_profissional = input('Digite a função profissional da pessoa: ')
pessoa_1.email = input('Digite o email da pessoa: ')
pessoa_1.telefone =  int(input('Digite o telefone da pessoa: '))

pessoa_2 = Pessoas()
pessoa_2.nome = input('Digite o nome da pessoa: ')
pessoa_2.data_nascimento = datetime.strptime(input('Digite a data de nascimento: DD/MM/AAAA'), '%d/%m/%Y').date()
pessoa_2.fun_profissional = input('Digite a função profissional da pessoa: ')
pessoa_2.email = input('Digite o email da pessoa: ')
pessoa_2.telefone =  int(input('Digite o telefone da pessoa: '))

pessoa_3 = Pessoas()
pessoa_3.nome = input('Digite o nome da pessoa: ')
pessoa_3.data_nascimento = datetime.strptime(input('Digite a data de nascimento: DD/MM/AAAA'), '%d/%m/%Y').date()
pessoa_3.fun_profissional = input('Digite a função profissional da pessoa: ')
pessoa_3.email = input('Digite o email da pessoa: ')
pessoa_3.telefone =  int(input('Digite o telefone da pessoa: '))

print(imprimir_cartao_visita)


idade = ((date.today() - self.data_nascimento) / 365).days





