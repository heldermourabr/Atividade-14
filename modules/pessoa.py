class Pessoa:
    nome, rg, endereco, contato = "", "", "", ""

    def __init__(self, nome, rg, endereco, contato):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato

    def set_nome(self, nome):
        self.nome = nome
    
    def set_rg(self, rg):
        self.rg = rg
    
    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def set_contato(self, contato):
        self.contato = contato

    def get_nome(self):
        return self.nome

    def get_rg(self):
        return self.rg
    
    def get_endereco(self):
        return self.endereco
    
    def get_contato(self):
        return self.contato
