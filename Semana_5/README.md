**Proyecto: Predicción de Supervivencia en el Titanic**

Este proyecto tiene como objetivo predecir si un pasajero del Titanic sobrevivió o no, utilizando varios modelos de aprendizaje supervisado de clasificación. El dataset del Titanic contiene información detallada sobre los pasajeros, lo que permite explorar diferentes características y su impacto en la supervivencia.

**Contenido del Notebook**
El notebook está estructurado en las siguientes secciones:

**Introducción:** 

Breve descripción del problema y los modelos a implementar.


**Carga de Datos:** 
Carga del dataset Titanic utilizando la librería seaborn.
Análisis Exploratorio de Datos (EDA): Análisis inicial de la distribución de las variables, la relación entre el sexo y la supervivencia, y la información general del dataset.


**Preprocesamiento:** 
Preparación de los datos para el entrenamiento de los modelos, incluyendo:
Selección de características relevantes (survived, pclass, sex, age, fare, embarked).
Manejo de valores nulos (eliminación de filas con NaN).
Transformación de variables categóricas (sex a numérico, embarked a variables dummy).


**Separación de Datos:** 
División del dataset en conjuntos de entrenamiento y prueba (X_train, X_test, y_train, y_test) utilizando train_test_split.


**Modelos de Clasificación:**
Implementación, entrenamiento y evaluación de los siguientes modelos:


**Regresión Logística:**
Un modelo lineal para problemas de clasificación.


**K-Nearest Neighbors (KNN):** 
Un algoritmo basado en la proximidad de los puntos de datos. Se incluye una optimización para encontrar el mejor valor de k.


**Árbol de Decisión:**
Un modelo que usa una estructura de árbol para tomar decisiones de clasificación.
Evaluación de Modelos: Para cada modelo, se calcula y muestra:
Accuracy.
Confusion Matrix (matriz de confusión) visualizada con un mapa de calor.
Classification Report (informe de clasificación) con precisión, recall y f1-score.


**Comparación de Modelos:**
Un resumen y visualización de la accuracy de cada modelo para identificar el de mejor rendimiento.


**Conclusión:** 
Resumen de los hallazgos y la importancia de comparar diferentes algoritmos.
Librerías Utilizadas
pandas: Para manipulación y análisis de datos.
seaborn: Para la carga del dataset y visualización de datos.
matplotlib.pyplot: Para la creación de gráficos.
sklearn: Para preprocesamiento de datos, implementación de modelos de clasificación y métricas de evaluación.
sklearn.model_selection.train_test_split
sklearn.linear_model.LogisticRegression
sklearn.neighbors.KNeighborsClassifier
sklearn.tree.DecisionTreeClassifier
sklearn.metrics.accuracy_score, confusion_matrix, classification_report

