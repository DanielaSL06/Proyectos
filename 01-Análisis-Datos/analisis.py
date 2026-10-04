import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats

def ejecutar_analisis():
    # 1. Entrada de la ruta del archivo
    print("--- Analizador Estadístico de Datos ---")
    ruta = r"c:\Users\danie\Downloads\RespuestasFormulario.csv" # Asegúrate que esta ruta sea la correcta
    ruta = ruta.replace('"', '').replace("'", "")

    if not os.path.exists(ruta):
        print(f"Error: No se encontró ningún archivo en la ruta: {ruta}")
        return

    # 2. Carga del archivo
    try:
        if ruta.lower().endswith('.csv'):
            df = pd.read_csv(ruta)
        elif ruta.lower().endswith(('.xlsx', '.xls')):
            df = pd.read_excel(ruta)
        else:
            print("Formato de archivo no soportado.")
            return
        print(f"\nArchivo cargado exitosamente. Filas: {df.shape[0]}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # 3. Limpieza de datos
    print("\n--- [1] Limpieza de Datos ---")
    columna_id = 'Número de expediente'
    if columna_id in df.columns:
        duplicados = df.duplicated(subset=[columna_id]).sum()
        df.drop_duplicates(subset=[columna_id], keep='first', inplace=True)
        print(f"- Expedientes duplicados eliminados: {duplicados}")

    # --- AJUSTE CRUCIAL: Convertir las 3 variables a números para que salgan en el Mapa ---
    col_y = 'En una escala del 1 al 100, ¿cuál es tu promedio actual en la carrera?'
    columnas_x = [
        '¿En cuántas materias utilizas la IA?',
        '¿Cuanto tiempo consideras que ahorras al utilizar la IA para realizar tus tareas?',
        'En una escala del 1 (nada) al 10 (mucho), ¿cuánto consideras que la IA ha mejorado tus calificaciones?'
    ]

    for col in [col_y] + columnas_x:
        if col in df.columns:
            # Esto convierte textos como "Mucho" en números (NaN) y luego los llena con la media
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(df[col].mean())

    # Manejo de valores nulos para el resto de las columnas
    columnas_con_nulos = df.columns[df.isnull().any()].tolist()
    for col in columnas_con_nulos:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    # 4. Estadística Descriptiva (Tu función original)
    def calcular_descriptiva(df):
        print("\n--- [2] Estadística Descriptiva ---")
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.empty: return
        estadisticas = pd.DataFrame({
          'Media': numeric_df.mean(),
          'Mediana': numeric_df.median(),
          'Moda': numeric_df.mode().iloc[0],
          'Mínimo': numeric_df.min(),
          'Máximo': numeric_df.max(),
          'Desviación Estándar': numeric_df.std(),
        })
        print(estadisticas.round(3).to_string())

    calcular_descriptiva(df)

    # 5. Análisis de Correlación (Mapa de Calor con TODAS las columnas numéricas)
    print("\n--- [3] Matriz de Correlación (Pearson) ---")
    numeric_df = df.select_dtypes(include=[np.number])

    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        plt.figure(figsize=(12, 10))
        # Ahora sí aparecerán las 3 variables de IA porque ya son numéricas
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt=".2f", annot_kws={"size": 8})
        plt.title("Mapa de Calor de Correlaciones (Todas las variables)")
        plt.tight_layout()
        plt.show()

    # 6. MODELOS DE REGRESIÓN PARA LAS 3 VARIABLES (Lo que te pidió la maestra)
    print("\n--- [4] Modelos de Regresión Lineal ---")
    Y = df[col_y]
    for i, col_x in enumerate(columnas_x, start=1):
        if col_x in df.columns:
            X = df[col_x]
            slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
            
            print(f"\nModelo {i}: {col_x}")
            print("-" * 50)
            print(f"Ecuación: y = {intercept:.2f} + {slope:.2f}x")
            print(f"r: {r_value:.4f} | r^2: {r_value**2:.4f} | p: {p_value:.4f}")
            
            # Gráfico de Dispersión individual
            plt.figure(figsize=(8, 5))
            sns.regplot(x=X, y=Y, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
            plt.title(f'Regresión: {col_x[:50]}...')
            plt.show()

if __name__ == "__main__":
    sns.set_theme(style="whitegrid")
    ejecutar_analisis()