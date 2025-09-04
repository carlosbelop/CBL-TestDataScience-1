import os
from pathlib import Path
import joblib
import pandas as pd

# Cargar modelo y nombres de clases
modelo, target_names = joblib.load("artifacts/best_model_RF.pkl")
BASE_DIR = Path('.').resolve().parent if (Path('.').resolve().name == 'src') else Path('.').resolve()
print(BASE_DIR)

def modo_interactivo():
    print("\n")
    print("🍷 Predicción de calidad de vino")
    print("Introduce las características:")

    # Pedir datos al usuario
    q1 = float(input("Fixed acidity: "))
    q2 = float(input("Volatile acidity: "))
    q3 = float(input("Citric acid: "))
    q4 = float(input("Residual Sugar: "))
    q5 = float(input("Chlorides: "))
    q6 = float(input("Free Sulfur Dioxide: "))
    q7 = float(input("Total Sulfur Dioxide: "))
    q8 = float(input("Density: "))
    q9 = float(input("pH: "))
    q10 = float(input("Sulphates: "))
    q11 = float(input("Alcohol: "))

    scaler = joblib.load(BASE_DIR / 'artifacts' / 'scaler.pkl')

    # Escalar las características antes de predecir
    features = [[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]]
    features_scaled = scaler.transform(features)

    # Hacer predicción
    pred = modelo.predict(features_scaled)[0]
    print(f"\n✅ Predicción: {target_names[pred]}")

def modo_batch():
    ruta = input("📂 Introduce la ruta del archivo CSV: ").strip()
    if not os.path.exists(ruta):
        print("❌ Ruta no válida. Asegúrate de que el archivo existe.")
    
    else:
        print(f"📊 Procesando archivo: {ruta}")
        df = pd.read_csv(ruta)

        # Verificar que el DataFrame tiene las columnas esperadas
        expected_columns = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                            "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
                            "pH", "sulphates", "alcohol"]
        if not all(col in df.columns for col in expected_columns):
            print("❌ El archivo CSV no contiene las columnas esperadas.")
            print(f"Columnas esperadas: {expected_columns}")
            print(f"Columnas encontradas: {list(df.columns)}")
        else:

            # Escalar las características antes de predecir
            scaler = joblib.load(BASE_DIR / 'artifacts' / 'scaler.pkl')
            features = df[expected_columns].values
            features_scaled = scaler.transform(features)

            # Hacer predicciones
            preds = modelo.predict(features_scaled)

            # Añadir predicciones al DataFrame original
            df['Predicción Calidad'] = [target_names[p] for p in preds]

            # Guardar resultados en un nuevo archivo CSV
            output_path = BASE_DIR / 'reports' / 'predicciones_calidad_vino.csv'
            df.to_csv(output_path, index=False)
            print(f"✅ Predicciones guardadas en: {output_path}")

if __name__ == "__main__":
    opcion = 0
    while opcion not in ["1", "2", "3"]:
        print("Elige modo de uso:")
        print("1 - Interactivo (inputs por terminal)")
        print("2 - CSV (ruta a archivo con datos)")
        print("3 - Salir\n")
        opcion = input("👉 Selección: ")

        if opcion == "1":
            modo_interactivo()
        elif opcion == "2":
            modo_batch()
        elif opcion == "3":
            print("👋 Saliendo...")
        else:
            print("❌ Opción no válida")