## Estructura del repositorio

Evaluación_Parcial/

├── Alquileres_RioGrande (Final).ipynb
├── Dataset_precios_alquiler_RioGrande_Final.xlsx
├── Informe Técnico - Predicción de Precios de Alquileres.docx
├── Diccionario de Datos.docx
├── README.md

Archivos históricos conservados:
- Entrega 1
- Dataset preliminar
- Versiones intermedias utilizadas durante el desarrollo del proyecto

## Predicción de Precios de Alquileres en Río Grande, Tierra del Fuego

Descripción del Proyecto:

Este proyecto tiene como objetivo desarrollar un modelo de Aprendizaje Automático capaz de predecir el precio de alquiler de propiedades ubicadas en la ciudad de Río Grande, provincia de Tierra del Fuego, Argentina.

A partir de información relevada de distintas inmobiliarias locales y portales inmobiliarios, se construyó un dataset con características descriptivas de cada inmueble para entrenar y evaluar distintos modelos de regresión.

Objetivo General:

Desarrollar y evaluar modelos de Machine Learning que permitan estimar el precio de alquiler de inmuebles en Río Grande utilizando características físicas, geográficas y comerciales de las propiedades.

Fuentes de Datos:

Los datos fueron relevados manualmente a partir de publicaciones inmobiliarias públicas:

•	Mac Rae Propiedades

•	Grupo Inversión

•	Inmobiliaria Latitud

•	Inmobiliaria Tierra del Fuego

•	Mercado Libre Inmuebles

Dataset:

Cantidad de registros analizados: 167 propiedades.

Variables utilizadas

•	Barrio

•	Ciudad

•	Ambientes

•	Metros²

•	Tipo_propiedad

•	Amoblado

•	Antigüedad

•	Baños

•	Cochera

•	Mascotas_permitidas

•	Expensas_incluidas

Análisis Exploratorio de Datos (EDA)

Se realizaron análisis descriptivos y visualizaciones para identificar patrones relevantes:

•	Distribución de precios.

•	Precio promedio por barrio.

•	Relación entre superficie y precio.

•	Precio según tipo de propiedad.

•	Identificación de valores atípicos.

Modelos Evaluados:

Regresión Lineal

•	MAE: 136.142

•	RMSE: 198.442

•	R²: 0.726

Árbol de Decisión:

•	MAE: 132.353

•	RMSE: 191.784

•	R²: 0.744

Random Forest:

•	MAE: 105.882

•	RMSE: 157.731

•	R²: 0.835

Mejor Modelo_
El modelo Random Forest obtuvo el mejor desempeño general, logrando explicar aproximadamente el 83,5% de la variabilidad observada en los precios de alquiler.

Tecnologías Utilizadas:

•	Python

•	Pandas

•	NumPy

•	Matplotlib

•	Seaborn

•	Scikit-Learn

•	Google Colab

•	Git

•	GitHub

Conclusiones:

Los resultados obtenidos demuestran que es posible construir modelos predictivos útiles para estimar precios de alquiler utilizando variables relacionadas con ubicación, superficie y características generales de los inmuebles.

Random Forest fue el modelo con mejor desempeño, convirtiéndose en la alternativa recomendada para futuras aplicaciones predictivas dentro del mercado inmobiliario local.

Autor:

Lionel Alfredo Martínez

Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial

Centro Politécnico Superior Malvinas Argentinas

Materia: Aprendizaje Automático

Año 2026

