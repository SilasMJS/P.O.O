# Paradigma Imperativo - Fortran - Sequência, Decisão e a Iteração
# Paradigma Estruturado - C - structs
# Paradigma Procedural - Python 

def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome,'idade': idade, 'cpf': cpf, 'email': email}
    return paciente


#  reúso e Coesão

# Paradigma Orientado à Objetos

# Classe - um conjunto de objetos com as mesmas características
# Objeto - Representação do mundo real com um tipo de dados de uma classe
# Construtor - É a função criada implicitamente com o mesmo nome da classe
# Atributo - São as variáveis de uma classe

class Paciente:
    
    def __init__(self, nome, idade, cpf, email):
        print("Acessei o Construtor")
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.email = email
        
        
# reúso e a Coesão
# Acoplamento, herança, polimorfismo, GAP semântico

# simulação de Eventos Discretos -> Paradigma Orientado á Objetos
# Relação -> Destacando funções e variáveis


"""
Visibilidade - Modificador de Acesso

Privada (Private) - restritiva -> Define que os atributos e métodos só podem ser manipulados dentro da classe.
Protegida (Protected) - intermediária -> Define que os atributos e métodos só podem ser manipulados dentro da classe
e nas classes que herdam a classe onde foram definidos.
Pública (Public) - menos restritiva -> Define que os atributos e métodos são acessivéis em qualquer lugar.
"""

# Arquivo *****BANCO******
class Conta:
    # Atributo de Classe
    taxa = 0.50
    
    @classmethod
    def retornarCodigo(cls):
        print('Codigo: 555')
    
    @staticmethod
    def retornarCodigoBanco():
        return '345'
    
    # Atributos de Instâncias
    def __init__(self, numero, titular, saldo=2000):
        self.__numero = numero
        self.titular = titular
        self.saldo = saldo
        
    def extrato(self):
        print(f'Saldo: R${self.saldo}')
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
        
    
# Instâncias de Classe Conta
conta1 = Conta(123, 'João Carlos', 2000)
conta2 = Conta(456, 'Maria Antonieta', 2000)

print(conta1.titular)
print(conta2.titular)

print(conta1.__dict__)
print(conta2.__dict__)
        