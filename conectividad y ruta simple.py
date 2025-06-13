from collections import deque

class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        if vertice1 in self.adjacencias and vertice2 in self.adjacencias:
            self.adjacencias[vertice1].append(vertice2)
            self.adjacencias[vertice2].append(vertice1)

    def es_conexo(self):
        if not self.adjacencias:
            return True  # Un grafo vacío es considerado conexo.
        
        visitados = set()
        vertices = list(self.adjacencias.keys())
        
        # Usamos BFS desde un vértice arbitrario
        self._bfs(vertices[0], visitados)

        return len(visitados) == len(self.adjacencias)

    def _bfs(self, inicio, visitados):
        cola = deque([inicio])
        visitados.add(inicio)

        while cola:
            vertice = cola.popleft()
            for vecino in self.adjacencias[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

    def encontrar_camino(self, inicio, fin):
        if inicio not in self.adjacencias or fin not in self.adjacencias:
            return []  # Devuelve lista vacía si el vértice no existe.

        padres = {inicio: None}
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)

        while cola:
            vertice = cola.popleft()

            if vertice == fin:
                return self._reconstruir_camino(padres, inicio, fin)

            for vecino in self.adjacencias[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice
                    cola.append(vecino)

        return []  # Si no se encuentra el camino, devuelve lista vacía.

    def _reconstruir_camino(self, padres, inicio, fin):
        camino = []
        actual = fin

        while actual is not None:
            camino.append(actual)
            actual = padres[actual]

        camino.reverse()  # Invertimos el camino para que esté en orden de inicio a fin.
        return camino

def main():
    grafo = Grafo()
    
    # Ingreso de vértices
    vertices = input("Ingrese los vértices del grafo separados por comas: ").split(',')
    for vertice in vertices:
        grafo.agregar_vertice(vertice.strip())

    # Ingreso de aristas
    while True:
        arista = input("Ingrese una arista en el formato 'v1,v2' (o 'fin' para terminar): ")
        if arista.lower() == 'fin':
            break
        v1, v2 = arista.split(',')
        grafo.agregar_arista(v1.strip(), v2.strip())

    # Verificar si el grafo es conexo
    print("El grafo es conexo:", grafo.es_conexo())

    # Encontrar caminos
    inicio = input("Ingrese el vértice de inicio: ")
    fin = input("Ingrese el vértice de fin: ")
    camino = grafo.encontrar_camino(inicio.strip(), fin.strip())
    if camino:
        print(f"Camino de '{inicio}' a '{fin}':", camino)
    else:
        print(f"No hay camino de '{inicio}' a '{fin}'.")

if __name__ == "__main__":
    main()
