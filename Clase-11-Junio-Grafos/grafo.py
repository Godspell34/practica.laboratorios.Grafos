"""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  Implementación de Grafo en Python                                         ║
║  Versión: 1.0.0                                                            ║
║  Fecha: 11 de Junio, 2025                                                  ║
║  Autores:                                                                  ║
║    - Alex Diaz                                                             ║
║    - Ssler Flores                                                          ║
║                                                                            ║
║  Descripción:                                                              ║
║  Esta clase implementa una estructura de datos Grafo que puede ser         ║
║  dirigida o no dirigida. Permite agregar vértices y aristas, obtener       ║
║  vecinos de un vértice y verificar la existencia de aristas. Las aristas   ║
║  pueden tener pesos opcionales.                                            ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

from collections import deque

# Clase Grafo
class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    # Agregar un vértice al grafo. Si el vértice ya existe, no hace nada.
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    # Agregar una arista entre dos vértices. Si no existe el vértice, se agrega.
    def agregar_arista(self, u, v, peso=1):
        if u not in self.grafo:
            self.agregar_vertice(u)
        if v not in self.grafo:
            self.agregar_vertice(v)
        self.grafo[u].append((v, peso))
        if not self.es_dirigido:
            self.grafo[v].append((u, peso))

    # Obtener los vecinos de un vertice. 
    def obtener_vecinos(self, vertice):
        return [v[0] for v in self.grafo.get(vertice, [])] # Si el vertice no existe, devuelve una lista vacia
    
    def existe_arista(self, u, v):
        return any(v == vecino[0] for vecino in self.grafo.get(u, [])) # Si existe una arista entre u y v, devuelve True
    
    def es_conexo(self):
        # Casos especiales
        if not self.grafo:  # Grafo vacío
            return True
        if len(self.grafo) == 1:  # Un solo vértice
            return True
            
        # Seleccionar un vértice inicial arbitrario
        vertice_inicial = next(iter(self.grafo))
        
        # Realizar BFS desde el vértice inicial
        visitados = set()
        cola = deque([vertice_inicial])
        visitados.add(vertice_inicial)
        
        while cola:
            vertice_actual = cola.popleft()
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        # El grafo es conexo si todos los vértices fueron visitados
        return len(visitados) == len(self.grafo)
    
    def encontrar_camino(self, inicio, fin):
        # Verificar que los vértices existen
        if inicio not in self.grafo or fin not in self.grafo:
            return []
            
        # Si inicio y fin son el mismo vértice
        if inicio == fin:
            return [inicio]
            
        # Inicializar estructuras de datos
        visitados = set()
        cola = deque([inicio])
        padres = {inicio: None}  # Diccionario para almacenar los padres de cada vértice
        
        # Marcar el vértice inicial como visitado
        visitados.add(inicio)
        
        # BFS para encontrar el camino
        while cola:
            vertice_actual = cola.popleft()
            
            # Si encontramos el vértice final
            if vertice_actual == fin:
                # Reconstruir el camino
                camino = []
                while vertice_actual is not None:
                    camino.append(vertice_actual)
                    vertice_actual = padres[vertice_actual]
                return camino[::-1]  # Invertir el camino para que vaya de inicio a fin
            
            # Explorar vecinos
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    cola.append(vecino)
        
        # Si no se encontró camino
        return []
    
if __name__ == "__main__":
    # Crear el grafo del Ejercicio 1
    grafo = Grafo(es_dirigido=False)
    
    # Agregar vértices
    for vertice in ['A', 'B', 'C', 'D', 'E']:
        grafo.agregar_vertice(vertice)
    
    # Agregar aristas
    aristas = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'D'),
        ('D', 'E')
    ]
    for origen, destino in aristas:
        grafo.agregar_arista(origen, destino)
    
    print("Grafo del Ejercicio 1:")
    print("Vértices:", grafo.vertices)
    print("Aristas:", grafo.aristas)
    print("\nPruebas de conectividad:")
    print(f"¿El grafo es conexo?: {grafo.es_conexo()}")
    
    print("\nPruebas de caminos:")
    print(f"Camino de A a E: {grafo.encontrar_camino('A', 'E')}")
    print(f"Camino de A a F (vértice inexistente): {grafo.encontrar_camino('A', 'F')}")