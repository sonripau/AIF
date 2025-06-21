import numpy as np
from collections import defaultdict
import time
from functools import wraps

class MetricasBusqueda:
    """
    Clase para almacenar y calcular métricas de algoritmos de búsqueda:
    - E: Nodos explorados
    - F: Nodos en frontera
    - d: Profundidad de la solución
    - g: Costo total
    """

    def __init__(self):
        # Estructura: métricas[map_size][rep][alg] = np.array([E, F, d, g])
        self.métricas = defaultdict(lambda: defaultdict(dict))

    def registrar(self, tamaño, repetición, algoritmo, E, F, d, g):
        """Registra una tupla de métricas para un tamaño, repetición y algoritmo específicos."""
        self.métricas[tamaño][repetición][algoritmo] = np.array([E, F, d, g])

    def promedios(self):
        """Calcula el promedio por algoritmo y tamaño de mapa."""
        promedios_por_tamaño = {}
        for tamaño, repeticiones in self.métricas.items():
            promedios_por_tamaño[tamaño] = {}
            for algoritmo in next(iter(repeticiones.values())).keys():
                valores = [repeticiones[rep][algoritmo] for rep in repeticiones]
                promedios_por_tamaño[tamaño][algoritmo] = np.mean(valores, axis=0)
        return promedios_por_tamaño

    def mostrar_resultados(self):
        """Imprime los promedios por tamaño y algoritmo."""
        promedios = self.promedios()
        for tamaño, algoritmos in promedios.items():
            print(f"\nTamaño de mapa: {tamaño}")
            for algoritmo, (E, F, d, g) in algoritmos.items():
                print(f"  Algoritmo: {algoritmo} → E: {E:.2f}, F: {F:.2f}, d: {d:.2f}, g: {g:.2f}")


def timed(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        output = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[TIMING] '{func.__name__}' ran in {elapsed:.4f}s")
        return output
    return inner
