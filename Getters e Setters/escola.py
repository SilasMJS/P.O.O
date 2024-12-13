class Aluno:
    def __init__(self, nome, idade, matricula) -> None:
        self.__nome = nome 
        self.__idade = idade
        self.__matricula = matricula
        self.__notas = None
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        
    

aluno1 = Aluno('Silas', 15, 123456)
print(aluno1.nome)
print(aluno1.idade)

aluno1.idade = 24

print(aluno1.idade)

