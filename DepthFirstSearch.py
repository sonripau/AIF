from PlanificadorBase import PlanificadorRuta
from Nodo import NodoBusqueda
from Metricas import timed

class BusquedaProfundidad(PlanificadorRuta):
    """
    Implementación del algoritmo de búsqueda en profundidad (Depth-First-Search).
    Utiliza una pila (LIFO) para explorar el espacio de estados.
    """
    @timed
    def ejecutar(self):
        # Nodo inicial
        inicio = NodoBusqueda(
            self.terreno.inicio,
            self.terreno.orientacion_inicio,
            0,  # coste
            0,  # profundidad
            "Inicio"
        )

        pila = [inicio]  # estructura LIFO
        explorados = {(inicio.posicion, inicio.orientacion)}

        while pila:
            actual = pila.pop()
            self.examinados.append(actual)
            self.reportero.registrar_nodo(actual)

            # <<< CAMBIO: usar lista de nodos examinados del reportero
            self.reportero.examinados.append(actual)

            # Comprobar si es meta
            if self.es_objetivo(actual):
                #return self.reportero.mostrar_ruta(actual, mostrar_heuristica=True)

                d, g = self.reportero.mostrar_ruta(actual, mostrar_heuristica=True)

                # Se añande E y F antes del return
                E = len(explorados)  # explorados reales
                F = len(pila)  # pila = frontera actual en DFS
                return d, g, E, F
            
            # Generar sucesores
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
                    #self.frontera.append(nuevo)
                    self.reportero.en_frontera.append(nuevo)

        # Si no se encuentra solución
        print("The path to the goal was not found..")
        return None, None
