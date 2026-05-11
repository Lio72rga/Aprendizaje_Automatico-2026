Comparación de Modelos de Clasificación: SVM vs SGD
Descripción del proyecto
En este trabajo se realizó una comparación entre dos modelos de clasificación supervisada utilizando Python y la librería Scikit-learn.
Los modelos implementados fueron:
Support Vector Machine (SVM)
SGDClassifier (Stochastic Gradient Descent)
El objetivo del proyecto fue predecir la supervivencia de pasajeros del Titanic a partir de distintas variables del dataset.

Objetivo
Aplicar y comparar dos algoritmos de clasificación vistos en clase para resolver un problema de aprendizaje automático supervisado.

Dataset utilizado
Se utilizó el dataset Titanic, disponible en la librería Seaborn.
Variables utilizadas:
survived
pclass
sex
age
fare

Tecnologías y librerías utilizadas
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn

Modelos implementados
Support Vector Machine (SVM)
SVM busca encontrar un hiperplano que separe las clases con el mayor margen posible.
SGDClassifier
SGD utiliza el método de optimización Stochastic Gradient Descent para entrenar modelos de clasificación de manera eficiente.

Etapas del proyecto
Carga del dataset
Limpieza y preparación de datos
Transformación de variables
División en entrenamiento y prueba
Escalado de datos
Entrenamiento de modelos
Evaluación de métricas
Comparación de resultados

Métricas utilizadas
Accuracy
Classification Report
Confusion Matrix

Resultados
Ambos modelos lograron buenos resultados de clasificación.
El modelo SVM obtuvo una mejor precisión general en comparación con SGDClassifier.
SGDClassifier presentó un entrenamiento más rápido, aunque con una leve disminución en el rendimiento predictivo.

Conclusión
A partir del análisis realizado, se observó que ambos modelos pueden resolver correctamente el problema de clasificación propuesto.
Sin embargo, el modelo SVM presentó un mejor desempeño general en las métricas evaluadas, logrando una mayor capacidad de predicción sobre el conjunto de prueba.
Por este motivo, se considera que SVM fue el modelo más adecuado para este dataset.

Autor
Lionel Alfredo Martínez
