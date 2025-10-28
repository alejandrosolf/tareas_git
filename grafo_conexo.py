# Definición del grafo a partir de los datos proporcionados
NODOS = list(range(50))
ARISTAS = [
    {0, 29}, {0, 46}, {0, 21}, {0, 14}, {0, 38}, {0, 31}, {1, 41}, {1, 31}, {1, 21}, {1, 17}, 
    {2, 9}, {2, 26}, {2, 5}, {2, 25}, {2, 4}, {3, 18}, {3, 30}, {3, 47}, {4, 28}, {4, 9}, 
    {4, 8}, {5, 44}, {5, 12}, {6, 37}, {6, 10}, {7, 23}, {7, 22}, {7, 39}, {9, 19}, {9, 28}, 
    {9, 27}, {11, 33}, {13, 25}, {13, 38}, {13, 29}, {14, 26}, {14, 28}, {14, 39}, {15, 22}, 
    {15, 31}, {15, 19}, {15, 41}, {16, 46}, {16, 26}, {16, 38}, {16, 27}, {17, 40}, {17, 29}, 
    {18, 45}, {18, 42}, {18, 35}, {18, 33}, {18, 47}, {20, 36}, {20, 49}, {20, 42}, {22, 26}, 
    {22, 34}, {23, 31}, {23, 32}, {23, 40}, {24, 31}, {24, 44}, {25, 38}, {26, 31}, {27, 32}, 
    {29, 48}, {29, 41}, {30, 47}, {30, 37}, {33, 36}, {33, 49}, {34, 48}, {35, 45}, {36, 45}, 
    {37, 49}, {37, 45}, {37, 47}, {38, 41}, {40, 48}, {41, 44}, {42, 49}, {43, 48}, {45, 47}
]

def construir_lista_adyacencia(nodos, aristas):
    """Construye la lista de adyacencia del grafo."""
    adj = {node: [] for node in nodos}
    for edge in aristas:
        u, v = tuple(edge)
        adj[u].append(v)
        adj[v].append(u)
    return adj

ADJACENCIA = construir_lista_adyacencia(NODOS, ARISTAS)

def dfs(u, adj, visitados, componente_actual):
    """Implementación recursiva del algoritmo de Búsqueda en Profundidad (DFS)."""
    # 1. Marcar el nodo actual como visitado
    visitados.add(u)
    # 2. Agregar el nodo a la componente conexa actual
    componente_actual.append(u)
    
    # 3. Recorrer los vecinos
    for v in adj[u]:
        # Si el vecino no ha sido visitado, llamar a DFS recursivamente
        if v not in visitados:
            dfs(v, adj, visitados, componente_actual)

def encontrar_componentes_conexas(nodos, adj):
    """Encuentra todos los subgrafos conexos de un grafo."""
    visitados = set()
    componentes = []
    
    # Iterar sobre todos los nodos
    for nodo in nodos:
        # Si el nodo no ha sido visitado, es el inicio de una nueva componente
        if nodo not in visitados:
            componente_actual = []
            # Iniciar DFS para explorar toda la componente
            dfs(nodo, adj, visitados, componente_actual)
            # Almacenar la componente encontrada
            componentes.append(sorted(componente_actual))
            
    return componentes

# Ejecución del algoritmo y reporte de resultados
componentes_conexas = encontrar_componentes_conexas(NODOS, ADJACENCIA)

print("--- Resultado del Análisis de Componentes Conexas (DFS) ---")
print(f"El grafo tiene {len(NODOS)} nodos y {len(ARISTAS)} aristas.")
print(f"Número de subgrafos conexos encontrados: {len(componentes_conexas)}\n")

for i, componente in enumerate(componentes_conexas):
    print(f"Subgrafo Conexo {i+1} (Tamaño: {len(componente)}):")
    # Imprimir los vértices en formato de lista para el reporte
    print(f"Vértices: {componente}\n")

