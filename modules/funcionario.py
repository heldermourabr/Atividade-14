from modules.pessoa import Pessoa

class Funcionario(Pessoa):
    id_func, cargo = "", ""

    def __init__(self, nome, rg, endereco, contato, id_func, cargo):
        self.id_func = id_func
        self.cargo = cargo
        super().__init__(nome, rg, endereco, contato)

    def set_id_func(self, id_func):
        self.id_func = id_func
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    def get_id_func(self):
        return self.id_func

    def get_cargo(self):
        return self.cargo