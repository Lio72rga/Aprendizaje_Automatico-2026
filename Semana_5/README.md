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

### Análisis y Explicación de la Optimización de K en KNN

El gráfico de 'Optimización de K en KNN' muestra cómo la precisión (Accuracy) del modelo K-Nearest Neighbors varía según el número de vecinos (`k`) que se consideran. El valor de `k` es un hiperparámetro crucial en KNN: un `k` muy pequeño puede hacer que el modelo sea sensible al ruido en los datos, mientras que un `k` muy grande puede hacer que el modelo sea demasiado general y pierda detalles importantes.

#### ¿Cómo se realiza la optimización?

1.  **Iteración sobre `k`**: El código itera a través de diferentes valores de `k`, desde 1 hasta 10 en este caso.
2.  **Entrenamiento y Predicción**: Para cada valor de `k`, se entrena un nuevo modelo `KNeighborsClassifier` con `n_neighbors=k` utilizando los datos de entrenamiento (`X_train`, `y_train`). Luego, se usa este modelo para predecir las etiquetas en el conjunto de prueba (`X_test`).
3.  **Cálculo de Accuracy**: La `accuracy_score` entre las predicciones (`pred`) y las etiquetas reales (`y_test`) se calcula para cada `k` y se almacena en la lista `scores`.
4.  **Visualización**: Finalmente, se grafica el `accuracy` obtenido para cada `k` contra los valores de `k` (`range(1,11)`). El eje X representa el valor de `K` y el eje Y representa la `Accuracy`.

#### ¿Cómo se visualiza e interpreta en el gráfico?

*   **El Eje X (`Valor de K`)**: Indica el número de vecinos que el algoritmo KNN está considerando para clasificar un nuevo punto de datos.
*   **El Eje Y (`Accuracy`)**: Muestra la precisión del modelo en el conjunto de prueba para ese `k` particular. Una mayor precisión indica un mejor rendimiento del modelo.

Al observar el gráfico, el objetivo es encontrar el valor de `k` donde la línea de `Accuracy` alcanza su punto más alto (o se estabiliza en un valor alto). Este punto representa el `k` óptimo que equilibra el sesgo y la varianza, proporcionando el mejor rendimiento predictivo del modelo KNN para este conjunto de datos. Si el gráfico muestra fluctuaciones, se buscará el `k` con la precisión más consistentemente 


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

