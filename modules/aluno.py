from modules.pessoa import Pessoa

class Aluno(Pessoa):
    matricula = ""

    def __init__(self, nome, rg, endereco, contato, matricula):
        self.matricula = matricula
        super().__init__(nome, rg, endereco, contato)

    def set_matricula(self, matricula):
        self.matricula = matricula
    
    def get_matricula(self):
        return self.matricula
    