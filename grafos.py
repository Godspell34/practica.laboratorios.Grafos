import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
    # Si el vértice no está en el diccionario, lo añade con un conjunto vacío de vecinos
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vértice '{vertice}' agregado.")
            # Obtener vecinos de los vértices en el grafo dirigido
        else:
            print(f"Vértice '{vertice}' ya existe.")
    def agregar_arista(self, u, v, peso=1):
        # Asegurarse de que ambos vértices existan en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
    
        # Añadir la arista
        self.grafo[u].add(v)
        print(f"Arista {u} -> {v} agregada.")
    
        # Si no es dirigido, añadir la arista en la dirección opuesta también
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} (bidireccional) agregada.")
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])  # Convertir a lista para devolver
        return []  # Si el vértice no existe, no tiene vecinos
    def existe_arista(self, u, v):
        # Verifica si ambos vértices existen y si 'v' está en la lista de adyacencia de 'u'
        return u in self.grafo and v in self.grafo[u]
    def bfs(self, inicio):
        # Conjunto para guardar los vértices ya visitados
        visitados = set()
        # Cola para los vértices a visitar
        cola = collections.deque()
    
        # Empezar el recorrido desde el vértice inicial
        cola.append(inicio)
        visitados.add(inicio)
    
        recorrido = []  # Lista para almacenar el orden de visita
    
        while cola:
            # Sacar el primer elemento de la cola
            vertice_actual = cola.popleft()
            # Añadir el vértice actual al recorrido
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
    
            # Añadir a la cola los vecinos no visitados
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
    
        return recorrido
    def dfs(self, inicio):
        visitados = set()
        recorrido = []
    
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")
    
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
    
        # Iniciar el DFS desde el vértice dado
        _dfs_recursivo(inicio)
        return recorrido
    def imprimir_grafo(self):
        print("\n--- Representación del Grafo ---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {', '.join(vecinos)}")
        print()
    def es_conexo(self):
        if not self.grafo:
            return True
    
        # Tomar el primer vértice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))
    
        # Realizar un BFS desde el primer vértice
        recorrido_bfs = self.bfs(primer_vertice)
    def encontrar_camino(self, inicio, fin):
        # Verificar si los vértices de inicio y fin existen en el grafo
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no existen en el grafo.")
            return []
    
        # Inicializar la cola, el conjunto de vértices visitados y el diccionario de padres
        cola = collections.deque()
        visitados = set()
        padres = {}  # Para reconstruir el camino: padres[hijo] = padre
    
        # Agregar el vértice de inicio a la cola y al conjunto de visitados
        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None  # El vértice de inicio no tiene padre
    
        while cola:
            vertice_actual = cola.popleft()
    
            # Si hemos llegado al vértice de destino, reconstruir el camino
            if vertice_actual == fin:
                camino = []
                temp = fin
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino[::-1]  # Invertir el camino para que vaya de inicio a fin
    
            # Explorar los vecinos del vértice actual
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual  # Guardar el padre
                    cola.append(vecino)
    
        # Si llegamos aquí, no se encontró un camino
        return []
# --- EJECUCIÓN DEL EJEMPLO COMPLETO ---
print(" --- Creación de Grafo No Dirigido --- ")
mi_grafo = Grafo(es_dirigido=False)

# Agregar aristas al grafo
mi_grafo.agregar_arista('Managua', 'Masaya')
mi_grafo.agregar_arista('Managua', 'León')
mi_grafo.agregar_arista('Masaya', 'Granada')
mi_grafo.agregar_arista('Granada', 'Rivas')
mi_grafo.agregar_arista('Managua', 'Granada')  # Arista adicional para mayor conectividad

# Imprimir el grafo
mi_grafo.imprimir_grafo()

print("\n --- Operaciones Básicas --- ")
# Obtener vecinos de un vértice
print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")

# Verificar existencia de arista
print(f"¿Existe arista entre Managua y Masaya? {mi_grafo.existe_arista('Managua', 'Masaya')}")
print(f"¿Existe arista entre Managua y Rivas? {mi_grafo.existe_arista('Managua', 'Rivas')}")

print("\n --- Recorridos --- ")
# Recorrido BFS y DFS desde Managua
print(f"Orden de recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
print(f"Orden de recorrido DFS desde Managua: {mi_grafo.dfs('Managua')}")

print("\n --- Conectividad y Caminos --- ")
# Verificar si el grafo es conexo
print(f"¿Es el grafo conexo? {mi_grafo.es_conexo()}")
# Encontrar camino entre dos vértices
camino = mi_grafo.encontrar_camino('Managua', 'Rivas')
print(f"Camino de Managua a Rivas: {camino}")

# Intentar encontrar un camino entre vértices que no tienen conexión
camino_inexistente = mi_grafo.encontrar_camino('Managua', 'Juigalpa')
print(f"Camino de Managua a Juigalpa: {camino_inexistente}")

# --- Probar con un grafo dirigido ---
print("\n --- Creación de Grafo Dirigido ---")
grafo_dirigido = Grafo(es_dirigido=True)

# Agregar aristas al grafo dirigido
grafo_dirigido.agregar_arista('Inicio', 'A')
grafo_dirigido.agregar_arista('A', 'B')
grafo_dirigido.agregar_arista('B', 'C')
grafo_dirigido.agregar_arista('C', 'Fin')
grafo_dirigido.agregar_arista('Inicio', 'D')
grafo_dirigido.agregar_arista('D', 'Fin')

# Imprimir el grafo dirigido
grafo_dirigido.imprimir_grafo()
# Obtener vecinos de los vértices en el grafo dirigido
print(f"Vecinos de Inicio (dirigido): {grafo_dirigido.obtener_vecinos('Inicio')}")
print(f"Vecinos de Fin (dirigido): {grafo_dirigido.obtener_vecinos('Fin')}") # Debería ser vacío

# Verificar existencia de aristas en el grafo dirigido
print(f"¿Existe arista de A a B? {grafo_dirigido.existe_arista('A', 'B')}")
print(f"¿Existe arista de B a A? {grafo_dirigido.existe_arista('B', 'A')}") # Debería ser False

print("\n --- Recorridos en Grafo Dirigido ---")
# Realizar recorridos BFS y DFS en el grafo dirigido
print(f"Orden de recorrido BFS desde Inicio: {grafo_dirigido.bfs('Inicio')}")
print(f"Orden de recorrido DFS desde Inicio: {grafo_dirigido.dfs('Inicio')}")

print("\n --- Conectividad y Caminos en Grafo Dirigido ---")
# La conectividad no es tan directamente aplicable a grafos dirigidos sin modificar la definición
# pero podemos encontrar caminos entre vértices
camino_dirigido = grafo_dirigido.encontrar_camino('Inicio', 'Fin')
print(f"Camino dirigido de Inicio a Fin: {camino_dirigido}")

camino_dirigido_no_existente = grafo_dirigido.encontrar_camino('Fin', 'Inicio')
print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")
