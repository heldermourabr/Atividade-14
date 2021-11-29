from modules.aluno import Aluno

class Portugues(Aluno):
    nota = 0

    def __init__(self, nome, rg, endereco, contato, matricula, nota):
        self.nota = nota
        super().__init__(nome, rg, endereco, contato, matricula)
    
    def set_nota(self, nota):
        self.nota = nota

    def get_nota(self):
        return self.nota