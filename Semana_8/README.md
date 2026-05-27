Clase 8 - Aprendizaje No Supervisado
Segmentación de Clientes con K-Means
Objetivos
Aplicar K-Means para descubrir segmentos latentes de clientes.
Utilizar escalado de variables con StandardScaler.
Validar el número óptimo de clusters mediante el método del codo.
Evaluar el modelo utilizando Silhouette Score.
Interpretar perfiles de clientes mediante análisis de centroides.
Visualizar clusters utilizando gráficos y PCA.


Dataset utilizado
El dataset contiene información de comportamiento de clientes:

purchase_freq_month
avg_basket_usd
time_on_site_min
discount_sensitivity
returns_rate

También incluye variables de ruido:

noise_gauss
noise_uniform

Estas últimas fueron excluidas del clustering.


Tecnologías utilizadas
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn


Metodología
Carga y exploración de datos
Selección de variables
Escalado con StandardScaler
Método del codo
Entrenamiento con K-Means
Evaluación con Silhouette Score
Análisis de centroides
Visualización de clusters
Reducción de dimensionalidad con PCA


Resultados
Se identificaron 3 segmentos principales de clientes.
El modelo logró separar adecuadamente los grupos.
Los clusters permitieron detectar:
clientes sensibles a promociones
clientes premium
clientes con alta tasa de devoluciones


Conclusión
Este proyecto demuestra cómo aplicar técnicas de aprendizaje no supervisado para segmentar clientes y detectar patrones ocultos en los datos.

La combinación de clustering, análisis de centroides y visualización permite obtener información útil para estrategias de marketing y toma de decisiones.


Bibliografía
Han, R. (2019). Matemáticas del Aprendizaje Automático.
Jones, H. (2019). Aprendizaje Automático para principiantes.
Russell, R. (2018). Machine Learning paso a paso con Python.
