# 01. Analizador Estadístico de Datos y Prueba de Hipótesis

## Especificaciones Técnicas
* **Lenguaje de programación:** Python (v3.10 / v3.11)
* **Librerías utilizadas:**
  * `pandas`: Carga de archivos (CSV/Excel), limpieza de datos, eliminación de duplicados e imputación de nulos.
  * `numpy`: Procesamiento numérico y manipulación de estructuras de datos.
  * `scipy` (`scipy.stats`): Regresiones lineales (`linregress`), cálculo de p-values, r, r² y densidades de probabilidad normal.
  * `matplotlib`: Renderizado de la Campana de Gauss para pruebas de hipótesis y personalización de ejes y anotaciones.
  * `seaborn`: Generación del Mapa de Calor de correlación de Pearson (`heatmap`) y gráficos de dispersión con línea de tendencia (`regplot`).
* **Herramientas de entorno:** VS Code, Jupyter Notebook / Terminal de Python.

---

## Descripción del Proyecto
Este proyecto aborda un estudio estadístico completo sobre el impacto del uso de herramientas de Inteligencia Artificial en el rendimiento académico de estudiantes universitarios, procesando un conjunto de datos real recopilado mediante formularios.

El desarrollo se divide en dos módulos principales:

1. **Módulo de Análisis Exploratorio y Regresión (`analisis.py`):**
   * **Limpieza e ingesta:** Carga automática de archivos CSV/Excel, deduplicación de registros basada en el número de expediente y conversión explícita de variables cualitativas a numéricas con imputación de valores faltantes por la media.
   * **Estadística Descriptiva:** Cálculo de métricas clave (media, mediana, moda, mínimos, máximos y desviación estándar) para evaluar la tendencia central y dispersión.
   * **Matriz de Correlación:** Visualización del grado de asociación entre variables cuantitativas mediante un mapa de calor de Pearson.
   * **Modelado de Regresión Lineal:** Evaluación de modelos para analizar la relación entre la cantidad de materias con IA, el tiempo ahorrado y la percepción de mejora respecto al promedio académico ($Y$), calculando la ecuación de la recta ($y = a + bx$), coeficientes de determinación ($r^2$) y niveles de significancia ($p$-value).

2. **Módulo de Prueba de Hipótesis (`hipotesis.py`):**
   * **Distribución Normal (Campana de Gauss):** Graficación paramétrica del criterio de aceptación y rechazo para una prueba bilateral con nivel de significancia $\alpha = 0.05$ ($Z_{\text{crítico}} = \pm 1.96$).
   * **Evaluación del Z Calculado:** Representación visual de la región de rechazo de la hipótesis nula ($H_0$), demarcando gráficamente valores observados extremos ($Z = 17.744$).

---

## Instrucciones de Ejecución
1. Asegurarse de tener Python 3.x instalado.
2. Instalar las dependencias necesarias:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
