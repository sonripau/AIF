class InformeBusqueda:
    """Clase auxiliar que muestra y registra el proceso de exploración de un algoritmo de búsqueda. 
    Imprime los nodos visitados (si está en modo verbose=True) y reconstruye la ruta final desde el inicio hasta el objetivo,
    facilitando la comprensión y análisis del recorrido realizado."""
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.examinados = []
        self.en_frontera = []

    def registrar_nodo(self, nodo):
        # Imprime info nodo actual si está activado el modo verbose
        if self.verbose:
            print(f"Exploring the node coord {nodo.posicion}, orientation='{nodo.orientacion}', cost={nodo.coste}, depth={nodo.profundidad}")

    def mostrar_ruta(self, nodo_final, mostrar_heuristica=False):
        """
        Reconstruye e imprime la ruta desde el nodo inicial hasta el nodo objetivo.
        Si mostrar_heuristica=True, también muestra el valor de la heurística (h) de cada nodo.
        """
        camino = []
        # Reconstruir la ruta hacia atrás, desde el nodo final hasta el inicial
        while nodo_final:
            camino.append(nodo_final)
            nodo_final = nodo_final.padre
        camino.reverse() # Se invierte para mostrar desde el inicio al objetivo

        print("\n>> Path from start to goal:")
        for i, paso in enumerate(camino):
            if i == 0:
                if mostrar_heuristica:
                    print(f"Node {i} (starting node): (d={paso.profundidad}, g(n)={paso.coste}, op=Start, h(n)={paso.heuristica}, S=({paso.posicion}, '{paso.orientacion}'))")
                else:
                    print(f"Node {i} (starting node): (d={paso.profundidad}, g(n)={paso.coste}, op=Start, S=({paso.posicion}, '{paso.orientacion}'))")
            else:
                print(f"Operator {i}: {paso.accion}")
                if mostrar_heuristica:
                    print(f"Node {i}: (d={paso.profundidad}, g(n)={paso.coste}, op={paso.accion}, h(n)={paso.heuristica}, S=({paso.posicion}, '{paso.orientacion}'))")
                else:
                    print(f"Node {i}: (d={paso.profundidad}, g(n)={paso.coste}, op={paso.accion}, S=({paso.posicion}, '{paso.orientacion}'))")

        print(f"\nTotal number of nodes explored: {len(self.examinados)}")
        print(f"Total number of nodes in frontier: {len(self.en_frontera)}")

        return camino[-1].profundidad, camino[-1].coste

"""
        print("\n>> Path from start to goal:")
        for i, paso in enumerate(camino):
            if i == 0:
                print(f"Node {i} (starting node): (d={paso.profundidad}, g(n)={paso.coste}, op=Start, S=({paso.posicion}, '{paso.orientacion}'))")
            else:
                print(f"Operator {i}: {paso.accion}")
                print(f"Node {i}: (d={paso.profundidad}, g(n)={paso.coste}, op={paso.accion}, S=({paso.posicion}, '{paso.orientacion}'))")

        print(f"\nTotal number of nodes explored: {len(self.examinados)}")
        print(f"Total number of nodes in frontier: {len(self.en_frontera)}")

        # Devuelve la profundidad y el coste total del último nodo (objetivo)
        return camino[-1].profundidad, camino[-1].coste

"""
"""        print("\n>> Path from start to goal:")
        for i, paso in enumerate(camino):
            if i == 0:
                print(f"Node {i} (starting node): Position: {paso.posicion}, Orientation: '{paso.orientacion}', Depth: {paso.profundidad}, Accumulated cost: {paso.coste}")
            else:
                print(f"Operator {i}: {paso.accion}")
                print(f"Node {i}: Position: {paso.posicion}, Orientation: '{paso.orientacion}', Depth: {paso.profundidad}, Accumulated cost: {paso.coste}")

        print(f"\nTotal number of nodes explored: {len(self.examinados)}")
        print(f"Total number of nodes in frontier: {len(self.en_frontera)}")

        # Devuelve la profundidad y el coste total del último nodo (objetivo)
        return camino[-1].profundidad, camino[-1].coste

        print("\n>> Path found from start to goal:")
        for i, paso in enumerate(camino):
            if mostrar_heuristica:
                print(f"[{i}] Pos: {paso.posicion}, Ori='{paso.orientacion}', Coste={paso.coste}, Prof={paso.profundidad}, h={paso.heuristica}, Op={paso.accion}")
            else:
                print(f"[{i}] Pos: {paso.posicion}, Ori='{paso.orientacion}', Coste={paso.coste}, Prof={paso.profundidad}, Op={paso.accion}")
        
        print(f"\nTotal de nodos explorados: {len(self.examinados)}")
        print(f"Total de nodos en frontera: {len(self.en_frontera)}")
        # Devuelve la profundidad y el coste total del último nodo (objetivo)
        return camino[-1].profundidad, camino[-1].coste

"""
