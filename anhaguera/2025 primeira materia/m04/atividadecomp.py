# Importar bibliotecas
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Converter as classes para One-Hot Encoding
encoder = OneHotEncoder(sparse=False)
y_encoded = encoder.fit_transform(y)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Construir o modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=50, batch_size=5, verbose=1)

# Avaliar o modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'\nAcurácia do modelo nos dados de teste: {accuracy:.2f}')

# Fazer previsões
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
sample_scaled = scaler.transform(sample)
prediction = model.predict(sample_scaled)
predicted_class = np.argmax(prediction)
print(f'Predição da nova flor: {iris.target_names[predicted_class]}')
