class Aluno:
    def __init__(self) -> None:
        self.nome = None
        self.data_nascimento = None
        self.cpf = None
        self.rg = None
        # atributos exclusivos para aluno
        self.matricula = None
        self.notas = None
        
    def estudar(self):
        return "Estudando..."

class Professor:
    def __init__(self) -> None:
        
        # atributos exclusivos para professor
        self.disciplina = None