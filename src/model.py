from pymongo import MongoClient
import joblib
import pandas

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
        
        self.registrar_usuario(nome, email, senha)


    def registrar_usuario(self, nome, email, senha):
        self.usuarios.insert_one({"nome": nome,
                                  "email": email,
                                  "senha": senha})

    
    def model_login(self, email, senha):

        login = self.usuarios.find_one({"email": email, "senha": senha})
        if not login:
            raise ValueError('login invalido')
        
        self.logar_usuario(login)

    def logar_usuario(self, login):
        self.usuario_logado = login

        
    def model_calculo(self, exercicio, carga, repeticao, genero, idade, peso):

        if carga == "" or repeticao == "" or idade == "" or peso == "":
            raise ValueError('campo vazio')
        elif not carga.isdigit() or not repeticao.isdigit() or not idade.isdigit() or not peso.isdigit():
            raise ValueError('digite apenas numeros')
        
        repeticao_maxima = self.calculo_maxima(carga, repeticao)

        nivel_usuario = self.classificar_nivel(exercicio, repeticao_maxima, genero, idade, peso)

        self.resultado = {"exercicio": exercicio,
                          "nivel": nivel_usuario,
                          "repeticao_maxima": repeticao_maxima}
        
    def calculo_maxima(self, carga, repeticao):
        # fórmula de epley para calcular a repetição maxima do usuario
        repeticao_maxima = float(carga) * (1 + float(repeticao) / 30)
        return repeticao_maxima
    
    def classificar_nivel(self, exercicio, repeticao_maxima, genero, idade, peso):
        niveis = ['AVANÇADO', 'INICIANTE', 'INTERMEDIÁRIO']

        exercicio_dic = {
            "SUPINO": 2,
            "DEADLIFT": 1,
            "AGACHAMENTO": 0
        }

        genero_dic = {
            "MASCULINO": 1,
            "FEMININO": 0
        }

        dados_usuario = pandas.DataFrame([
            {'exercicio': exercicio_dic[exercicio],
             'genero': genero_dic[genero],
             'idade': idade,
             'peso_corporal': peso,
             'peso_exercicio': repeticao_maxima}
        ])


        modelo_knn = joblib.load('knn/modelo_knn.pkl')

        predicao = modelo_knn.predict(dados_usuario)
        return niveis[predicao[0]]

    def get_usuario_logado(self):
        return self.usuario_logado
    
    def model_logout(self):
        self.usuario_logado = None

    def get_resultado(self):
        return self.resultado
    