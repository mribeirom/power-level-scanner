from pymongo import MongoClient

class Model:
    def __init__(self):
        
        self.client = MongoClient('mongodb://localhost:27017')
        self.data_base = self.client['power_level_scanner']

        self.usuarios = self.data_base.get_collection('usuarios')

        self.usuario_logado = None
        self.resultado = None

    def model_registro(self, nome, email, senha):

        if nome == "" or email == "" or senha == "":
            raise ValueError('campo vazio')
        
        elif self.usuarios.find_one({"email": email}):
            raise ValueError('email cadastrado')

        self.usuarios.insert_one({"nome": nome,
                                  "email": email,
                                  "senha": senha})
    
    def model_login(self, email, senha):

        login = self.usuarios.find_one({"email": email, "senha": senha})
        if not login:
            raise ValueError('login invalido')
        
        self.usuario_logado = login
        
    def model_calculo(self, exercicio, peso, repeticao):
        
        if peso == "" or repeticao == "":
            raise ValueError('campo vazio')
        elif not peso.isdigit() or not repeticao.isdigit():
            raise ValueError('digite apenas numeros')

        # fórmula de epley para calcular a repetição maxima do usuario
        repeticao_maxima = float(peso) * (1 + float(repeticao) / 30)

        self.resultado = {"exercicio": exercicio,
                          "nivel": "INTERMEDIARIO",
                          "repeticao_maxima": repeticao_maxima}

    def get_usuario_logado(self):
        return self.usuario_logado
    
    def model_logout(self):
        self.usuario_logado = None

    def get_resultado(self):
        return self.resultado
    