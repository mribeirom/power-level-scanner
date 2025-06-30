from model import Model

class Controller:
    def __init__(self, view):

        self.model = Model()
        self.view = view
    
    def controller_registro(self, nome, email, senha):
        try:
            self.model.model_registro(nome, email, senha)
            self.view.registro_sucesso()
        except ValueError as e:
            if str(e) == 'campo vazio':
                self.view.registro_mensagem_erro('CAMPO VAZIO')
            elif str(e) == 'email cadastrado':
                self.view.registro_mensagem_erro('E-MAIL JÁ CADASTRADO')
    
    def controller_login(self, email, senha):
        try:
            self.model.model_login(email, senha)
            self.view.login_sucesso()
        except ValueError as e:
            if str(e) == 'login invalido':
                self.view.login_mensagem_erro('LOGIN INVÁLIDO')
    
    def controller_calculo(self, exercicio, carga, repeticao, genero, idade, peso):
        try:
            self.model.model_calculo(exercicio, carga, repeticao, genero, idade, peso)
            self.view.calculo_sucesso()
        
        except ValueError as e:
            if str(e) == 'campo vazio':
                self.view.calculo_mensagem_erro('CAMPO VAZIO')

            elif str(e) == 'digite apenas numeros':
                self.view.calculo_mensagem_erro('DIGITE APENAS NÚMEROS')

    def solicitar_usuario_logado(self):
        return self.model.get_usuario_logado()
    
    def controller_logout(self):
        self.model.model_logout()
        self.view.mostrar_tela_login()
    
    def solicitar_resultado(self):
        return self.model.get_resultado()
