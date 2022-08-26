from datetime import datetime,date

class Pessoa:
    
    nome = None
    data_nascimento = None
    fun_profissional = None
    email = None
    telefone = None
    
    
    def imprimir_cartao_visita(self):
        idade = ((date.today() - self.data_nascimento) / 365).days
        print(f'Nome: {self.nome} \nIdade: {idade} \nFunção profissional: {self.fun_profissional} \nemail: {self.email} \nTelefone: {self.telefone}\n\n\n ')
        
        

pessoa_1 = Pessoa()
pessoa_1.nome = input('Digite o nome da pessoa: ')
pessoa_1.data_nascimento = datetime.strptime(input('Digite a data de nascimento: DD/MM/AAAA'), '%d/%m/%Y').date()
pessoa_1.fun_profissional = input('Digite a função profissional da pessoa: ')
pessoa_1.email = input('Digite o email da pessoa: ')
pessoa_1.telefone =  int(input('Digite o telefone da pessoa: '))

pessoa_2 = Pessoa()
pessoa_2.nome = input('Digite o nome da pessoa: ')
pessoa_2.data_nascimento = datetime.strptime(input('Digite a data de nascimento: DD/MM/AAAA'), '%d/%m/%Y').date()
pessoa_2.fun_profissional = input('Digite a função profissional da pessoa: ')
pessoa_2.email = input('Digite o email da pessoa: ')
pessoa_2.telefone =  int(input('Digite o telefone da pessoa: '))

pessoa_3 = Pessoa()
pessoa_3.nome = input('Digite o nome da pessoa: ')
pessoa_3.data_nascimento = datetime.strptime(input('Digite a data de nascimento: DD/MM/AAAA'), '%d/%m/%Y').date()
pessoa_3.fun_profissional = input('Digite a função profissional da pessoa: ')
pessoa_3.email = input('Digite o email da pessoa: ')
pessoa_3.telefone =  int(input('Digite o telefone da pessoa: '))

pessoa_1.imprimir_cartao_visita()
pessoa_2.imprimir_cartao_visita()
pessoa_3.imprimir_cartao_visita()




