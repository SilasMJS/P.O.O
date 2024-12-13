
class Gato:
    def __init__(self,nome,peso,idade,raça):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raça = raça
        self.dono = None
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    @property
    def peso(self):
        return self.__peso

    @property
    def idade(self):
        return self.__idade

    @property
    def raça(self):
        return self.__raça

    def adotado(self,dono):
        self.dono = dono

class Pessoa:
    def __init__(self,nome,endereço,cpf):
        self.__nome = nome
        self.__endereço = endereço
        self.__cpf = cpf
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def endereço(self):
        return self.__endereço

    @endereço.setter
    def endereço(self,endereço):
        self.__endereço = endereço
    @property
    def cpf(self):
        return self.__cpf
    
    
# execução #
mimi = Gato("Sem nome",2,1,"SRD")
joao = Pessoa("João da Silva","Rua das Flores, 123","123.456.789-00")
mimi.adotado(joao)
print(mimi.dono.nome)
mimi.nome = "Tommy"
print(mimi.nome)

maria = Pessoa("Maria Santos","Avenida Principal, 456","987.654.321-00")
mingau = Gato("Mingau",1,0.5,"SRD")
print(mingau.dono)
mingau.adotado(maria)
print(mingau.dono.nome)

