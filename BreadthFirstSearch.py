# bfs.py

from collections import deque
from Nodo import NodoBusqueda
from PlanificadorBase import PlanificadorRuta
from Metricas import timed

class BusquedaAnchura(PlanificadorRuta):
    """
    Implementación del algoritmo de búsqueda por anchura (Breadth-First-Search).
    Recorre los nodos en orden de menor profundidad primero, utilizando una cola FIFO.
    """
    @timed
    def ejecutar(self):
        # Nodo inicial
        inicio = NodoBusqueda(
            self.terreno.inicio,
            self.terreno.orientacion_inicio,
            0,        # Coste acumulado
            0,        # Profundidad (nivel)
            "Inicio"  # Acción inicial
        )

        pila = deque([inicio])  # Cola de nodos por explorar
        explorados = {(inicio.posicion, inicio.orientacion)}  # Conjunto de nodos visitados

        while pila:
            actual = pila.popleft()  # Tomar el nodo más antiguo

            # usa lista de nodos examinados del reportero
            self.reportero.examinados.append(actual)

            # registrar nodo con verbose si corresponde
            self.reportero.registrar_nodo(actual)

            # Comprobación de objetivo
            if self.es_objetivo(actual):
                # mostrar métricas
                d, g = self.reportero.mostrar_ruta(actual, mostrar_heuristica=True)

                # Se añade E y F antes del return
                E = len(explorados)  # explorados reales
                F = len(pila)  # pila = frontera actual en BFS
                return d, g, E, F
            
            # Generar sucesores del nodo actual
            for pos, ori, coste, accion in self.movimientos_posibles(actual):
                clave = (pos, ori)
                if clave not in explorados:
                    nuevo = NodoBusqueda(
                        pos,
                        ori,
                        actual.coste + coste,
                        actual.profundidad + 1,
                        accion,
                        nodo_previo=actual
                    )
                    pila.append(nuevo)
                    explorados.add(clave)

                    # usa lista de frontera del reportero
                    self.reportero.en_frontera.append(nuevo)
                    
        # Si no se encuentra solución        
        print("The path to the goal was not found.")
        return None, None