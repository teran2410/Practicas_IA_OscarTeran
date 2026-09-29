# Importar las librerías necesarias
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el dataset del vino
wine = load_wine()
X, y = wine.data, wine.target

# Dividir los datos: 80% para entrenamiento y 20% para prueba con semilla 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el clasificador
clf = DecisionTreeClassifier(max_depth=None, random_state=42)
clf.fit(X_train, y_train)

"""
En la práctica, lo que hicimos fue cargar el dataset de los vinos y dividir la información en dos partes: el 80% para que el modelo de árbol de decisión aprenda a clasificar y el 20% para ponerlo a prueba con datos que no conoce.   Cuando limitamos el árbol a una profundidad baja (max_depth=2), el modelo genera un esquema sencillo y directo que nos da una precisión aceptable (alrededor del 86%). Pero al quitarle el límite (max_depth=None), el árbol se vuelve más grande y toma en cuenta más características químicas, como las cenizas (ash) o el alcohol, lo que sube la precisión a cerca del 94%. Esto pasa porque el modelo se vuelve más específico para separar los grupos, aunque hay que tener cuidado de que no memorice de más los datos de entrenamiento.
"""

# Evaluar la precisión del modelo en los datos de prueba
y_pred = clf.predict(X_test)
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {precision * 100:.2f}%\n")

# Exportar y visualizar las reglas simbólicas
rules = export_text(clf, feature_names=list(wine.feature_names))
print("Reglas del Árbol de Decisión:")
print(rules)