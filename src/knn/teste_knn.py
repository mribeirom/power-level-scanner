import joblib
import pandas

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
    {'exercicio': exercicio_dic["SUPINO"],
        'genero': genero_dic["MASCULINO"],
        'idade': 20,
        'peso_corporal':80,
        'peso_exercicio': 160}
])


modelo_knn = joblib.load('modelo_knn.pkl')
scaler = joblib.load('scaler.pkl')

normalizar = ['idade', 'peso_corporal', 'peso_exercicio']
dados_usuario[normalizar] = scaler.transform(dados_usuario[normalizar])
predicao = modelo_knn.predict(dados_usuario)
print(niveis[predicao[0]]) 