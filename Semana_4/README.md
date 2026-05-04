
Este describe el contenido de este notebook de Google Colab, que implementa un modelo de Regresión Lineal simple.

README.md

# **Proyecto de Análisis de Regresión Lineal**
Este notebook de Google Colab presenta un ejemplo básico de Regresión Lineal utilizando un dataset sintético para predecir precios de viviendas.

**Estructura del Notebook**
El notebook está organizado en las siguientes secciones:
1. Importación de Librerías: Carga las bibliotecas necesarias como , , , , , y .pandasnumpymatplotlibseabornsklearn.model_selectionsklearn.linear_modelsklearn.metrics
   
2. Carga de Datos: Creación de un pequeño dataset sintético con 'área', 'habitaciones' y 'precio' de viviendas.
   
2. Exploración de Datos (EDA): Análisis descriptivo (, ) y visualización de relaciones entre variables (, ).df.info()df.describe()sns.pairplotsns.heatmap
   
4. Preparación de Datos: Identificación de variables predictoras (X) y variable objetivo (y). No se requiere limpieza adicional ya que el dataset es sintético y no tiene nulos ni categóricas.
   
5. División Train/Test: Separación del dataset en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.
 
6. Modelo de Regresión: Entrenamiento de un modelo de de .LinearRegressionscikit-learn

7. Evaluación: Medición del rendimiento del modelo utilizando métricas como el Error Absoluto Medio (MAE), Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R²).
   
8. Conclusiones: Resumen de los hallazgos y posibles mejoras futuras.

**Conjunto de datos**

El dataset utilizado es un conjunto de datos sintético y pequeño (7 registros) que simula características de viviendas (área y número de habitaciones) y sus precios. Es importante destacar que, debido a su tamaño, las correlaciones observadas son excepcionalmente altas y no suelen reflejar la complejidad de los datos reales.

**Resultados Clave**

**EDA:** Se observó una fuerte correlación lineal positiva entre el área, las habitaciones y el precio.

**Modelo:** El modelo de Regresión Lineal entrenado mostró un rendimiento casi perfecto (R² = 1.0) en el conjunto de prueba, lo cual es esperable dado el dataset sintético y altamente correlacionado.

**Métricas:** MAE y MSE son extremadamente bajos, lo que indica una predicción muy precisa sobre los datos de prueba.

**Actividad:** Modelo de Regresión Logística para Clasificación de Usuarios

Este repositorio contiene un ejercicio práctico de implementación de un modelo de Regresión Logística para clasificar usuarios basándose en su comportamiento en una plataforma web. El objetivo es predecir el sistema operativo (Windows, Mac, Linux) que utiliza un usuario.

Este ejercicio complementa el proyecto de Modelo de Regresión Lineal previamente subido, permitiendo explorar diferentes técnicas de modelado predictivo.

**Contenido del Repositorio**
usuarios_win_mac_lin.csv: El conjunto de datos utilizado para entrenar y evaluar el modelo.
actividad_regresion_logistica.ipynb: El notebook de Google Colab que documenta todo el proceso, desde la carga de datos hasta la evaluación del modelo.

**Descripción del Problema**
Se busca predecir la (sistema operativo) de un usuario basándose en las siguientes características de comportamiento:clase
duracion: Tiempo que el usuario pasa en la plataforma.

1. paginas: Número de páginas visitadas.

2. acciones: Cantidad de interacciones realizadas.
   
3. valor: Una métrica de valor o importancia del usuario.

4. Metodología
   
**Carga de Datos:**

Se carga el dataset en un DataFrame de Pandas.usuarios_win_mac_lin.csv

**Preparación de Datos:** División del dataset en conjuntos de entrenamiento y prueba.

**Entrenamiento del Modelo:** Se utiliza de Scikit-learn para entrenar el modelo.LogisticRegression

**Predicción:** Se realizan predicciones sobre el conjunto de prueba.

**Evaluación del Modelo:** Se evalúa el rendimiento del modelo utilizando métricas como , y .AccuracyMatriz de ConfusiónClassification Report

**Visualización:** Se genera un mapa de calor para la matriz de confusión para una mejor interpretación de los resultados.

**Resultados Clave**

El modelo de Regresión Logística alcanzó una del 67.6% en este dataset. La matriz de confusión reveló que el modelo tiene un buen desempeño en la clasificación de usuarios de Windows y Linux, pero presenta dificultades para identificar correctamente a los usuarios de Mac (clase 1), lo que sugiere un área de mejora.Accuracy

**Integración con el Modelo de Regresión Lineal**
Este ejercicio de clasificación utilizando Regresión Logística complementa el trabajo previo en Regresión Lineal. Mientras que la Regresión Lineal se enfoca en predecir valores continuos, la Regresión Logística es ideal para problemas de clasificación binaria o multiclase como este.

**Consideraciones para la integración:**

* **Comparación de Enfoques:** Se puede comparar cómo diferentes tipos de modelos abordan distintos problemas de negocio (predicción de un valor vs. clasificación de una categoría).

* **Flujo de Trabajo Común:** Se observa las similitudes en el flujo de trabajo (carga de datos, preprocesamiento, entrenamiento, evaluación) entre ambos tipos de modelos.

* **Ampliación del Portafolio:** Juntos, estos dos proyectos muestran la habilidad para aplicar tanto modelos de regresión como de clasificación, cubriendo un espectro más amplio de tareas de Machine Learning.
