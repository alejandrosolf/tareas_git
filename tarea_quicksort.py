import random
import time
import math
import matplotlib.pyplot as plt
import numpy as np

# =================================================================
# SECCIÓN 1: IMPLEMENTACIÓN DE QUICKSORT CON PIVOTE ALEATORIO
# =================================================================

def quicksort_particion_aleatoria(arr, inicio, fin):
    """Selecciona un pivote aleatorio, lo intercambia a la última posición y realiza la partición."""
    # 1. Elección aleatoria del pivote
    indice_pivote = random.randint(inicio, fin)
    # Coloca el pivote aleatorio al final para la partición
    arr[indice_pivote], arr[fin] = arr[fin], arr[indice_pivote]
    
    pivote = arr[fin]
    i = inicio - 1
    
    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Coloca el pivote en su posición final
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

def quicksort_aleatorio(arr, inicio, fin):
    """Función principal de QuickSort recursiva."""
    if inicio < fin:
        # q es el índice de partición
        q = quicksort_particion_aleatoria(arr, inicio, fin)
        # Llama recursivamente a las sublistas
        quicksort_aleatorio(arr, inicio, q - 1)
        quicksort_aleatorio(arr, q + 1, fin)

def ordenar_array(arr):
    """Función de envoltura para QuickSort."""
    quicksort_aleatorio(arr, 0, len(arr) - 1)

# =================================================================
# SECCIÓN 2: EXPERIMENTACIÓN, MEDICIÓN DE TIEMPOS Y CÁLCULO DE MEDIA
# =================================================================

# Tamaños de arreglos (n)
N = [100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000]
NUM_REPETICIONES = 50
tiempos_medios = []
tiempos_guardados = {} # Para almacenar todos los tiempos por si es necesario

print("Iniciando experimento Monte Carlo para QuickSort...")

for n in N:
    # Genera el arreglo base (0 a n-1)
    base_arr = list(range(n))
    tiempos_n = []
    
    for i in range(NUM_REPETICIONES):
        # Permuta el arreglo aleatoriamente
        arr_a_ordenar = base_arr[:]
        random.shuffle(arr_a_ordenar) 
        
        # Mide el tiempo de ejecución
        inicio = time.perf_counter()
        ordenar_array(arr_a_ordenar)
        fin = time.perf_counter()
        
        # Guarda el tiempo
        tiempos_n.append(fin - inicio)
    
    # Calcula la media y la guarda
    tiempo_medio_n = sum(tiempos_n) / NUM_REPETICIONES
    tiempos_medios.append(tiempo_medio_n)
    tiempos_guardados[n] = tiempos_n
    
    print(f"n={n}: Tiempo medio = {tiempo_medio_n:.6f} segundos")

# Convertir a array de numpy para cálculos de constantes
T_medios = np.array(tiempos_medios)

# =================================================================
# SECCIÓN 3: CÁLCULO DE CONSTANTES Y GRAFICACIÓN
# =================================================================

# 1. Definición de n=1000 y su tiempo experimental (índice 4 en N y T_medios)
n0 = 1000
T_exp_n0 = T_medios[N.index(n0)]

# 2. Cálculo de constantes k1 y k2
# k1 para O(n log n)
# Usamos log2 para ser consistentes con el análisis de complejidad
k1 = T_exp_n0 / (n0 * np.log2(n0))
# k2 para O(n^2)
k2 = T_exp_n0 / (n0**2)

print(f"\n--- Constantes Calculadas (punto de intersección n={n0}) ---")
print(f"k1 (O(n log n)): {k1:.6e}")
print(f"k2 (O(n^2)): {k2:.6e}")

# Funciones de complejidad teórica
def T_nlogn(n, k):
    # La complejidad O(n log n) se refiere a logaritmo binario o natural, aquí usamos binario.
    return k * n * np.log2(n)

def T_n2(n, k):
    return k * n**2

# Generar puntos para las curvas teóricas (para una gráfica suave)
N_plot = np.linspace(N[0], N[-1], 200) 
T_nlogn_teorico = T_nlogn(N_plot, k1)
T_n2_teorico = T_n2(N_plot, k2)

# Configuración de la gráfica
plt.figure(figsize=(10, 6))

# Gráfica de los resultados empíricos (puntos y línea)
plt.plot(N, T_medios, 'o-', label='Tiempo Promedio Empírico (QuickSort)', color='blue')

# Gráfica de O(n log n)
plt.plot(N_plot, T_nlogn_teorico, label=f'$O(n \log_2 n)$ con $k_1={k1:.2e}$', linestyle='--', color='green')

# Gráfica de O(n^2)
plt.plot(N_plot, T_n2_teorico, label=f'$O(n^2)$ con $k_2={k2:.2e}$', linestyle=':', color='red')

# Punto de intersección (n=1000)
plt.plot(n0, T_exp_n0, 'ks', markersize=8, label=f'Punto de Intersección $n={n0}$')

plt.xlabel('Tamaño del Arreglo (n)')
plt.ylabel('Tiempo Medio de Ejecución (segundos)')
plt.title('Desempeño Empírico de QuickSort Aleatorio')
plt.legend()
plt.grid(True, linestyle='dotted')
plt.show()

