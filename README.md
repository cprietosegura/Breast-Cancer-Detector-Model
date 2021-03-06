# Breast Cancer Detector

El cáncer de mama es el tipo de cáncer más frecuente entre las mujeres españolas. Aproximadamente una de cada ocho mujeres son diagnosticadas con cáncer de mama a lo largo de su vida. Hay una alta probabilidad de recuperación si el tumor es detectado en un estadio temprano.

Breast Cancer Detector (BCD) es una app  de machine learning desarrollado en `Python` con el `algoritmo Random Forest Classifier` de `Sklearn` para ayudar al personal médico en el diagnóstico de cáncer de mama. La idea parte de un dataset de `Kaggle` con más de 270.000 imagénes histopatológicas de tejido tumoral escaneadas a 40x. BCD detecta si el tejido tumoral contiene Carcinoma Ductal Invasivo, el más común de los tumores malignos de mama.

## Preparación de las imágenes

Organicé el dataset de imágenes, tratando las imágenes con las librerías `Numpy` y `OpenCV` para que todas tuvieran el formato adecuado para su procesamiento y entrenamiento con el algoritmo de machine learning.

## Entrenamiento 

`Random Forest Classifier` fue el algoritmo de clasificación de `Sklearn` que mejores métricas obtuvo a la hora de hacer la predicción de los tumores. Utilicé `GridSearchCV` para obtener los mejores parámetros con los que entrenar el algoritmo, con los que el modelo consigue un accuracy de más del 80%.

## API
Finalmente integré el modelo predictivo en una api desarrollada con `Flask` en entorno local, que permite cargar una imagen y devuelve el diagnóstico de dicha imagen, confirmando si el tumor es maligno o si es benigno. Esta es la interfaz de BCD: 

![alt text](https://github.com/cprietosegura/Breast-Cancer-Detector-Model/blob/master/notebooks/api_bcd.jpg)

Una vez cargada la imagen, se envía la consulta y devuelve el diagnóstico:

![alt text](https://github.com/cprietosegura/Breast-Cancer-Detector-Model/blob/master/notebooks/api_bcd_diagnosis.jpg)


