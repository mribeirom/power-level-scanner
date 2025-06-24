from model import Model

class Controller:
    def __init__(self, view):

        self.model = Model()
        self.view = view
    
    def controller_registro(self, nome, email, senha):
        return self.model.model_registro(nome, email, senha)
    
    def controller_login(self, email, senha):
        return self.model.model_login(email, senha)
    
    def controller_calculo(self, exercicio, peso, repeticao):
        return self.model.model_calculo(exercicio, peso, repeticao)