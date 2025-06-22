from abc import ABC, abstractmethod
from Navegation import Navegacion
from Reportero import InformeBusqueda

"""
This abstract base class (`PlanificadorRuta`) defines the common interface and logic 
for search-based path planning algorithms (e.g., BFS, DFS, A*) in a grid environment 
with orientation-aware robot movement.

Key Components:
- `terreno`: The terrain/grid the robot navigates, containing the map, costs, start and goal.
- `visitados`, `frontera`, `examinados`, `en_frontera`: Lists used to track explored and frontier nodes.
- `reportero`: Utility to print step-by-step search trace if verbose mode is enabled.

Key Methods:
- `ejecutar()`: Abstract method that must be implemented by subclasses to define the actual search logic.
- `es_objetivo(nodo)`: Checks if a given node is a goal state. If orientation is required, it must match as well.
- `movimientos_posibles(nodo)`: Returns a list of valid successor states (turn left, turn right, move forward).
  Forward movement is only allowed if it stays within bounds, and the terrain cost is used as the move cost.
  Turning always has a uniform cost of 1.

This class abstracts and encapsulates the motion model, making it reusable across different search algorithms.
"""
class PlanificadorRuta(ABC):
    def __init__(self, terreno, verbose=False):
        self.terreno = terreno
        self.visitados = []
        self.frontera = []
        self.examinados = []
        self.en_frontera = []
        self.reportero = InformeBusqueda(verbose)

    @abstractmethod
    def ejecutar(self):
        pass

    def es_objetivo(self, nodo):
        if self.terreno.orientacion_meta != "I":
            return (
                nodo.posicion == self.terreno.meta
                and nodo.orientacion == self.terreno.orientacion_meta
            )
        return nodo.posicion == self.terreno.meta

    def movimientos_posibles(self, nodo):
        pos, ori = nodo.posicion, nodo.orientacion
        if isinstance(ori, int):
            idx = ori
            ori = Navegacion.MAPEO_ENTERO_A_DIRECCION[ori]
        else:
            idx = Navegacion.DIRECCIONES.index(ori)
        movimientos = [
            (pos, Navegacion.DIRECCIONES[(idx + 1) % 8], 1, "Giro der."),
            (pos, Navegacion.DIRECCIONES[(idx - 1) % 8], 1, "Giro izq."),
        ]
        dx, dy = Navegacion.MOVIMIENTOS[ori]
        nueva_pos = (pos[0] + dx, pos[1] + dy)
        filas, columnas = self.terreno.dimensiones
        if 0 <= nueva_pos[0] < filas and 0 <= nueva_pos[1] < columnas:
            costo = self.terreno.grilla[nueva_pos[0]][nueva_pos[1]]
            movimientos.append((nueva_pos, ori, costo, "Avanzar"))
        return movimientos
