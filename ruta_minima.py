import heapq

# --- Datos del Grafo ---
# El grafo se representa como una lista de adyacencia
# adj[u] = [(v, weight), ...] donde (u) es el origen, (v) el destino y (weight) el peso.

# NOTA: Los datos proporcionados están en formato de aristas no dirigidas ({u, v, weight}).
# Para un DÍGRAFO, asumiremos que las aristas son dirigidas de u a v, con el peso dado.
# Si fuera un grafo NO DIRIGIDO, se añadiría la arista (v, u) con el mismo peso.
# Como el problema pide un DÍGRAFO, solo se considera la dirección (u) -> (v).

ARISTAS = [
    (0, 5, 1), (0, 7, 9), (0, 11, 11), (0, 16, 11), (0, 17, 3), (0, 18, 9), 
    (1, 5, 5), (1, 7, 1), (1, 9, 10), (1, 15, 1), (1, 16, 6), (1, 19, 12), 
    (2, 12, 14), (2, 16, 4), (2, 19, 13), (3, 7, 5), (3, 15, 1), (3, 16, 10), 
    (3, 18, 4), (4, 7, 3), (4, 8, 11), (4, 11, 12), (4, 13, 13), (4, 16, 9), 
    (4, 18, 8), (5, 7, 2), (5, 8, 2), (5, 9, 13), (5, 11, 1), (5, 14, 12), 
    (6, 7, 8), (6, 10, 6), (6, 13, 13), (6, 15, 5), (6, 18, 13), (7, 8, 2), 
    (7, 11, 13), (7, 16, 4), (7, 17, 6), (7, 19, 7), (8, 13, 8), (8, 14, 10), 
    (8, 16, 14), (9, 16, 9), (10, 17, 7), (10, 19, 5), (11, 13, 12), (11, 14, 13), 
    (11, 15, 2), (12, 13, 9), (12, 15, 7), (12, 17, 8), (13, 15, 1), (13, 18, 9), 
    (13, 19, 6), (14, 18, 9), (15, 18, 2), (17, 18, 14), (17, 19, 13)
]
NUM_NODOS = 20
INFINITO = float('inf')

def construir_grafo(aristas, num_nodos):
    """Convierte la lista de aristas a una lista de adyacencia."""
    adj = {i: [] for i in range(num_nodos)}
    for u, v, weight in aristas:
        # Arista dirigida: u -> v con peso 'weight'
        adj[u].append((v, weight))
    return adj

ADJACENCIA = construir_grafo(ARISTAS, NUM_NODOS)

def dijkstra(grafo, inicio, fin):
    """
    Implementa el algoritmo de Dijkstra para encontrar la ruta mínima.

    Args:
        grafo (dict): Lista de adyacencia.
        inicio (int): Nodo de inicio (origen).
        fin (int): Nodo final (destino).

    Returns:
        tuple: (distancia_minima, camino_reconstruido)
    """
    # 1. Inicialización
    # 'distancia' almacena la distancia mínima conocida desde el nodo de inicio.
    distancia = {i: INFINITO for i in range(NUM_NODOS)}
    distancia[inicio] = 0
    
    # 'previo' almacena el predecesor para reconstruir el camino.
    previo = {i: None for i in range(NUM_NODOS)}
    
    # Cola de prioridad: (distancia, nodo)
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        # Obtener el nodo con la menor distancia conocida (u)
        dist_u, u = heapq.heappop(cola_prioridad)

        # Si ya hemos encontrado una ruta más corta a 'u', ignorar esta entrada.
        if dist_u > distancia[u]:
            continue
            
        # Parar si llegamos al destino
        if u == fin:
            break

        # 2. Relajación: Revisar los vecinos (v) de (u)
        for v, peso in grafo.get(u, []):
            nueva_dist = dist_u + peso
            
            # Si se encuentra una ruta más corta a través de (u)
            if nueva_dist < distancia[v]:
                distancia[v] = nueva_dist
                previo[v] = u  # Actualizar el predecesor
                heapq.heappush(cola_prioridad, (nueva_dist, v)) # Añadir a la cola

    # 3. Reconstrucción del Camino
    camino = []
    actual = fin
    while actual is not None:
        camino.append(actual)
        actual = previo[actual]
        if actual == inicio:
            camino.append(inicio)
            break
        
    camino.reverse()

    # Si la distancia es INFINITO, no hay camino
    if distancia[fin] == INFINITO:
        return INFINITO, []
    
    return distancia[fin], camino

# --- Ejecución y Reporte ---
NODO_INICIO = 0
NODO_FIN = 14

distancia_minima, camino = dijkstra(ADJACENCIA, NODO_INICIO, NODO_FIN)

print("--- Ejecución del Algoritmo de Dijkstra ---")
print(f"Buscando la ruta mínima de: Nodo {NODO_INICIO} a Nodo {NODO_FIN}\n")

if distancia_minima == INFINITO:
    print(f"No se encontró un camino del nodo {NODO_INICIO} al nodo {NODO_FIN}.")
else:
    print(f"Distancia Mínima (Costo): {distancia_minima}")
    print(f"Ruta Mínima (Nodos): {' -> '.join(map(str, camino))}")
