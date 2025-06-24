from pymongo import MongoClient

class Model:
    def __init__(self):
        
        self.client = MongoClient('mongodb://localhost:27017')
        self.data_base = self.client['power_level_scanner']

        self.usuarios = self.data_base.get_collection('usuarios')

    
    def model_registro(self, nome, email, senha):

        if self.usuarios.find_one({"email": email}):
            return 1
        elif nome == "" or email == "" or senha == "":
            return 2

        self.usuarios.insert_one({"nome": nome,
                                  "email": email,
                                  "senha": senha})
        return 0
    
    def model_login(self, email, senha):
        login = self.usuarios.find_one({"email": email, "senha": senha})
        if login:
            return login
        else:
            return 1
        

    def model_calculo(self, exercicio, peso, repeticao):
        
        if peso == "" or repeticao == "":
            return 1
        elif not peso.isdigit() or not repeticao.isdigit():
            return 2

        # fórmula de epley
        repeticao_maxima = float(peso) * (1 + float(repeticao) / 30)

        resultado = {"exercicio": exercicio.upper(),
                     "nivel": "INTERMEDIARIO",
                     "repeticao_maxima": int(repeticao_maxima)}

        return resultado
        

