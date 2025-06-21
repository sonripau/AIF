from abc import ABC, abstractmethod
from Reportero import InformeBusqueda
from Navegation import Navegacion

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
            return nodo.posicion == self.terreno.meta and nodo.orientacion == self.terreno.orientacion_meta
        return nodo.posicion == self.terreno.meta

    def movimientos_posibles(self, nodo):
        pos, ori = nodo.posicion, nodo.orientacion
        idx = Navegacion.DIRECCIONES.index(ori)
        movimientos = [
            (pos, Navegacion.DIRECCIONES[(idx + 1) % 8], 1, "Giro der."),
            (pos, Navegacion.DIRECCIONES[(idx - 1) % 8], 1, "Giro izq.")
        ]
        dx, dy = Navegacion.MOVIMIENTOS[ori]
        nueva_pos = (pos[0] + dx, pos[1] + dy)
        filas, columnas = self.terreno.dimensiones
        if 0 <= nueva_pos[0] < filas and 0 <= nueva_pos[1] < columnas:
            costo = self.terreno.grilla[nueva_pos[0]][nueva_pos[1]]
            movimientos.append((nueva_pos, ori, costo, "Avanzar"))
        return movimientos
