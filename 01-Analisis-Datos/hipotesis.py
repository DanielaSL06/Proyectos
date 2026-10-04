import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Parámetros EXACTOS 
z_critico = 1.96
z_calculado = 17.744

# 2. Crear los datos para la Campana de Gauss
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='black', linewidth=2)

# 3. Sombrear la Zona de Aceptación en el centro (Verde)
x_acc = x[(x >= -z_critico) & (x <= z_critico)]
y_acc = y[(x >= -z_critico) & (x <= z_critico)]
plt.fill_between(x_acc, y_acc, color='lightgreen', alpha=0.5, label='Zona de Aceptación (No Rechazo H0)')

# 4. Sombrear las DOS Zonas de Rechazo (Rojo)
x_rej_der = x[x > z_critico]
y_rej_der = y[x > z_critico]
plt.fill_between(x_rej_der, y_rej_der, color='salmon', alpha=0.8, label='Zona de Rechazo (Alfa = 0.05)')

x_rej_izq = x[x < -z_critico]
y_rej_izq = y[x < -z_critico]
plt.fill_between(x_rej_izq, y_rej_izq, color='salmon', alpha=0.8)

# 5. Dibujar las líneas de los Z Críticos (-1.96 y +1.96)
plt.axvline(z_critico, color='red', linestyle='--', label=f'+Z Crítico = {z_critico}')
plt.axvline(-z_critico, color='red', linestyle='--', label=f'-Z Crítico = {-z_critico}')

# 6. Marcar dónde quedó tu Z Calculado (17.744)
plt.annotate(f'Z Calculado = {z_calculado}\n(Rompe la escala hacia la derecha)', 
             xy=(3.9, 0.02), xytext=(1.8, 0.15),
             arrowprops=dict(facecolor='darkblue', shrink=0.05, width=2, headwidth=8), 
             fontsize=11, color='darkblue', weight='bold',
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='darkblue', facecolor='white', alpha=0.8))

# 7. Textos profesionales
plt.title('Criterio de Aceptación y Rechazo (Prueba de Dos Colas)', fontsize=14, weight='bold')
plt.xlabel('Valores Estadísticos Z', fontsize=12)
plt.ylabel('Densidad de Probabilidad', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3, linestyle='--')

# 8. Mostrar gráfica
plt.tight_layout()
plt.show()