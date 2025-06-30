import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

class KNN:
    def __init__(self):
        self.dataset = None
        self.modelo_knn = KNeighborsClassifier(n_neighbors=3)

        self.encoder_exercicio = LabelEncoder()
        self.encoder_genero = LabelEncoder()
        self.encoder_nivel = LabelEncoder()

        self.scaler = StandardScaler()

        self.features_train = None
        self.features_test = None

        self.targets_train = None
        self.targets_test = None


    def carrega_dataset(self):
        # carrega os dados para o treinamento de uma planilha
        self.dataset = pandas.read_csv('dataset.csv', sep=';')

    def converter_numeros(self):
        # os atributos que são palavras são convertidos em numeros
        self.dataset['exercicio'] = self.encoder_exercicio.fit_transform(self.dataset['exercicio'])
        self.dataset['genero'] = self.encoder_genero.fit_transform(self.dataset['genero'])
        self.dataset['nivel'] = self.encoder_nivel.fit_transform(self.dataset['nivel'])

    def dividir_dataset(self):
        # separa os dados de entrada e saida
        features = self.dataset.iloc[:, :-1]
        targets = self.dataset.iloc[:, -1]

        # divide os dados de treinamento entre 80% de treino e 20% de teste
        self.features_train, self.features_test, self.targets_train, self.targets_test = train_test_split(features, targets, test_size=0.2, random_state=42)

    def normalizar_dados(self):

        # normalizar os dados
        normalizar = ['idade', 'peso_corporal', 'peso_exercicio']

        self.scaler.fit(self.features_train[normalizar])
        self.features_train[normalizar] = self.scaler.transform(self.features_train[normalizar])
        self.features_test[normalizar] = self.scaler.transform(self.features_test[normalizar])
        #dados com uma variação muito grande de tamanho podem dificultar na
        #classificação do algoritmo,o maior valor sempre vai ter um peso maior
        #para o modelo e normalizar os dados coloca todos osdados na mesma escala

    def treinamento_modelo(self):
        # treina o modelo
        self.modelo_knn.fit(self.features_train, self.targets_train)
    
    def teste_modelo(self):

        # usa os dados de teste para fazer previsões com o modelo
        targets_predicted = self.modelo_knn.predict(self.features_test)

        # calcula a acuraria do modelo (porcentagem de acerto)
        accuracy = accuracy_score(self.targets_test, targets_predicted)
        print("Acurácia do modelo KNN:", accuracy)


        report = classification_report(self.targets_test, targets_predicted)
        print("Relatório de classificação:")
        print(report)
    
        matrix = confusion_matrix(self.targets_test, targets_predicted)
        print("Matriz de confusão:")
        print(matrix)
    
    def salvar_modelo(self):
        # salvar o modelo
        joblib.dump(self.modelo_knn, 'modelo_knn.pkl')
        # salva o modelo de normalização
        joblib.dump(self.scaler, 'scaler.pkl')



    def treinar_modelo(self):
        self.carrega_dataset()
        self.converter_numeros()
        self.dividir_dataset()
        self.normalizar_dados()
        self.treinamento_modelo()

knn = KNN()

knn.treinar_modelo()
knn.teste_modelo()
knn.salvar_modelo()
