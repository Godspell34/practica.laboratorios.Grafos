"""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  Implementación de BFS y DFS en Grafos                                     ║
║  Versión: 1.0.0                                                            ║
║  Fecha: 11 de Junio, 2025                                                  ║
║                                                                            ║
║  1. Búsqueda en Amplitud (BFS):                                            ║
║     • Método: bfs(self, inicio)                                            ║ 
║     • Realiza recorrido BFS desde vértice inicial                          ║
║     • Retorna lista de vértices en orden de visita                         ║
║     • Requiere: cola (collections.deque) y conjunto de visitados           ║
║                                                                            ║
║  2. Búsqueda en Profundidad (DFS):                                         ║
║     • Método: dfs(self, inicio)                                            ║
║     • Realiza recorrido DFS desde vértice inicial                          ║
║     • Retorna lista de vértices en orden de visita                         ║
║     • Implementación: recursiva o iterativa con pila                       ║
║     • Requiere: conjunto de vértices visitados                             ║
║                                                                            ║
║  3. Casos de Prueba:                                                       ║
║     • Grafo no dirigido del Ejercicio 1                                    ║
║     • Pruebas con bfs('A') y dfs('A')                                      ║
║     • Caso especial: grafo desconexo (vértice 'F' aislado)                 ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

from collections import deque
from grafo import Grafo

def bfs(grafo: Grafo, inicio):
    
    # Verificar que el vértice inicial existe en el grafo
    if inicio not in grafo.vertices:
        raise ValueError(f"El vértice {inicio} no existe en el grafo")
    
    # Inicializar estructuras de datos
    visitados = set()  # Set para mantener registro de vértices visitados
    cola = deque([inicio])  # Cola para el recorrido BFS
    orden_visita = []  # Lista para almacenar el orden de visita
    
    # Marcar el vértice inicial como visitado
    visitados.add(inicio)
    
    # Mientras haya vértices en la cola
    while cola:
        # Obtener el siguiente vértice de la cola
        vertice_actual = cola.popleft()
        orden_visita.append(vertice_actual)
        
        # Obtener todos los vecinos del vértice actual
        for vecino in grafo.obtener_vecinos(vertice_actual):
            # Si el vecino no ha sido visitado
            if vecino not in visitados:
                # Marcarlo como visitado y agregarlo a la cola
                visitados.add(vecino)
                cola.append(vecino)
    
    return orden_visita

def dfs(grafo: Grafo, inicio):
    
    # Verificar que el vértice inicial existe en el grafo
    if inicio not in grafo.vertices:
        raise ValueError(f"El vértice {inicio} no existe en el grafo")
    
    # Inicializar estructuras de datos
    visitados = set()  # Set para mantener registro de vértices visitados
    pila = [inicio]  # Pila para el recorrido DFS. Se usa una lista como pila para ahorrar tiempo, con los metodos de append y pop. 
    orden_visita = []  # Lista para almacenar el orden de visita
    
    # Mientras haya vértices en la pila
    while pila:
        # Obtener el vértice actual de la pila
        vertice_actual = pila.pop()
        
        # Si el vértice no ha sido visitado
        if vertice_actual not in visitados:
            # Marcarlo como visitado y agregarlo al orden de visita
            visitados.add(vertice_actual)
            orden_visita.append(vertice_actual)
            
            # Agregar los vecinos a la pila en orden inverso
            # para mantener el orden correcto de visita
            for vecino in reversed(grafo.obtener_vecinos(vertice_actual)):
                if vecino not in visitados:
                    pila.append(vecino)
    
    return orden_visita

# Casos de prueba
if __name__ == "__main__":
    # Crear un grafo no dirigido
    grafo = Grafo()
    
    # Agregar vértices
    for vertice in ['A', 'B', 'C', 'D', 'E', 'F']:
        grafo.agregar_vertice(vertice)
    
    # Agregar aristas (grafo no dirigido)
    aristas = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'D'),
        ('D', 'E')
    ]
    for origen, destino in aristas:
        grafo.agregar_arista(origen, destino)
    
    print("Grafo creado:")
    print("Vértices:", grafo.vertices)
    print("Aristas:", grafo.aristas)
    print("\nPrueba de BFS desde 'A':")
    print(bfs(grafo, 'A'))
    print("\nPrueba de DFS desde 'A':")
    print(dfs(grafo, 'A'))
    
    # Prueba con vértice aislado 'F'
    print("\nPrueba con vértice aislado 'F':")
    print("BFS desde 'F':", bfs(grafo, 'F'))
    print("DFS desde 'F':", dfs(grafo, 'F'))
