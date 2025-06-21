from Heuristicas import heuristica_euclidea
import heapq
from PlanificadorBase import PlanificadorRuta
from Nodo import NodoBusqueda
from Metricas import timed

class BusquedaAEstrella(PlanificadorRuta):
    """
    Implementación del algoritmo A* usando la heurística de distancia euclídea.
    """
    def __init__(self, terreno, heuristica=heuristica_euclidea, verbose=False):
        super().__init__(terreno, verbose)
        self.heuristica_func = heuristica

    @timed
    def ejecutar(self):
        meta = self.terreno.meta
        # Nodo inicial
        inicio = NodoBusqueda(
            self.terreno.inicio,
            self.terreno.orientacion_inicio,
            0, # coste
            0, # profundidad
            "Inicio",
            h_valor=heuristica_euclidea(self.terreno.inicio, meta)
        )

        contador = 0
        pila = []
        heapq.heappush(pila, (inicio.coste + inicio.heuristica, contador, inicio))

        visitados = {(inicio.posicion, inicio.orientacion): 0}

        while pila:
            _, _, actual = heapq.heappop(pila)
            #self.examinados.append(actual)
            self.reportero.examinados.append(actual)
            self.reportero.registrar_nodo(actual)

            if self.es_objetivo(actual):
                #return self.reportero.mostrar_ruta(actual, mostrar_heuristica=True)
                d, g = self.reportero.mostrar_ruta(actual, mostrar_heuristica=True)

                # Se añade E y F antes del return
                E = len(visitados)  # explorados reales
                F = len(pila)  # pila = frontera actual en BFS
                return d, g, E, F
            
            for pos, ori, coste, accion in self.movimientos_posibles(actual):
                nuevo_coste = actual.coste + coste
                clave = (pos, ori)

                if clave not in visitados or nuevo_coste < visitados[clave]:
                    visitados[clave] = nuevo_coste
                    heur = heuristica_euclidea(pos, self.terreno.meta)
                    nuevo = NodoBusqueda(
                        pos,
                        ori,
                        nuevo_coste,
                        actual.profundidad + 1,
                        accion,
                        nodo_previo=actual,
                        h_valor=heur
                    )
                    contador += 1
                    heapq.heappush(pila, (nuevo.coste + heur, contador, nuevo))
                    #self.frontera.append(nuevo)
                    self.reportero.en_frontera.append(nuevo)

        print("No se encontró un camino hacia la meta.")
        return None, None
