
# CBL-TestDataScience-1

Proyecto de ciencia de datos desarrollado en formato Jupyter Notebook y exportado como HTML.

## 📊 Dataset  

- **Fuente**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/186/wine+quality)  
- **Instancias**:  
  - 1599 vinos tintos  
  - 4898 vinos blancos  
- **Atributos**: 11 variables fisicoquímicas (ej. acidez, alcohol, densidad) + 1 variable de salida (calidad, 0–10).  
- **Problema**: clasificación multiclase altamente **desbalanceada** (la mayoría de vinos son de calidad “normal”).  

---

Este proyecto utiliza el dataset **Wine Quality** de UCI ([Cortez et al., 2009](https://archive.ics.uci.edu/dataset/186/wine+quality)) para predecir la calidad de vinos tintos y blancos en tres clases:  


**Atributos:**

      1. fixed acidity
      2. volatile acidity
      3. citric acid
      4. residual sugar
      5. chlorides
      6. free sulfur dioxide
      7. total sulfur dioxide
      8. density
      9. pH
      10. sulphates
      11. alcohol
      Output variable (based on sensory data): 
      12. quality (score between 0 and 10)


**Objetivo:**  
Clasificar la calidad de los vinos en tres categorías creadas a partir de `quality`:
- `malo`  : quality ∈ [0, 4]
- `normal`: quality ∈ [5, 6]
- `bueno` : quality ∈ [7, 10]

Se trabaja con ambos datasets (vino tinto y blanco). El pipeline incluye:
- Carga y unión de datos.
- Preprocesado y creación de etiquetas.
- EDA y análisis del desbalance de clases.
- Selección de variables (ANOVA, mutual information, RFE, RandomForest importance).
- Entrenamiento y evaluación de modelos (LogisticRegression, kNN, RandomForest, SVC).
- Guardado de resultados.



## ⚙️ Installation

Crear un entorno de conda o un entorno virtual con Python==3.13.0 e instalar las dependencias:

```bash
pip install -r requirements.txt

```
Clonar el repositorio e ir ejecutando el notebook.

--Opcional--  
En vez de clonar el repositorio, es suficiente descargando el notebook:

Una vez instalado los paquetes, descargar el notebook **CBL-TestDataScience-1.ipynb** e ir ejecutándolo en orden.  
Conforme avance la ejecución, se irá creando el repositorio con los directorios y los resultados.

## Deployment

Después de la instalación y ejecución del notebook, ejecutar **src/predict.py**

Seguir las instrucciones para hacer predicciones con el modelo obtenido, tanto manualmente introduciendo valores por terminal como mediante un archivo df (usar prueba_test.csv por ejemplo).



## 📂 Estructura del repositorio  

```
CBL-TestDataScience-1
├── artifacts                # Modelos y objetos serializados
│   ├── best_model_RF.pkl    # Modelo Random Forest entrenado (pickle)
│   └── scaler.pkl           # Escalador de datos guardado (pickle)
│
├── data                     # Datos del proyecto
│   └── raw                  # Datos en bruto (sin procesar)
│       ├── prueba_test.csv          # Conjunto de prueba para predict.py
│       ├── wine+quality.zip         # Archivo comprimido con dataset
│       ├── winequality-red.csv      # Datos de vino tinto
│       ├── winequality-white.csv    # Datos de vino blanco
│       └── winequality.names        # Descripción de las variables
│
├── notebooks                # Notebooks de experimentación
│   ├── CBL-TestDataScience-1.html   # Exportación en HTML del notebook
│   └── CBL-TestDataScience-1.ipynb  # Notebook principal con análisis y modelos
│
├── reports                  # Resultados y reportes del proyecto
│   ├── figures                        # Carpeta para figuras y gráficas
│   ├── feature_selection_summary.csv  # Resumen de selección de características
│   ├── model_comparison_results.csv   # Resultados de comparación de modelos
│   └── predicciones_calidad_vino.csv  # Predicciones finales del modelo
│
├── src                      # Código fuente del proyecto
│   └── predict.py           # Script para hacer predicciones con el modelo entrenado
│
├── .gitignore               # Archivos/carpetas ignorados por git
├── README.md                # Documentación principal del proyecto
└── requirements.txt         # Dependencias necesarias para reproducir el entorno

```

## 🤖 Modelos probados  

Se entrenaron los siguientes clasificadores con hiperparametrización:  

- **Logistic Regression**  
- **K-Nearest Neighbors (kNN)**  
- **Random Forest**  
- **Support Vector Machine (SVM)**  
- **Gradient Boosting**  
- **Multi-layer Perceptron (Neural Network)**  
- **Decision Tree**  
## References

- P. Cortez, A. Cerdeira, F. Almeida, T. Matos, J. Reis (2009). Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems, 47(4):547-553.

