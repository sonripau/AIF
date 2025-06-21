import csv
import os
import random

import numpy as np

from AStarSearch import BusquedaAEstrella
from BreadthFirstSearch import BusquedaAnchura
from DepthFirstSearch import BusquedaProfundidad
from Heuristicas import heuristica_euclidea
from Mapa import TerrenoExplorable

"""
output_dir = "resultados_busqueda"
os.makedirs(output_dir, exist_ok=True)

algoritmos = {
    "bfs": lambda terreno: BusquedaAnchura(terreno, verbose=False),
    "dfs": lambda terreno: BusquedaProfundidad(terreno, verbose=False),
    "a*": lambda terreno: BusquedaAEstrella(terreno, heuristica=lambda p: heuristica_euclidea(p, terreno.meta), verbose=False)
}

tamaños = [3, 5, 7, 9]
repeticiones = 10
semillas = np.random.randint(0, 10000, size=repeticiones)


def resolver_mapa(n, algoritmo, seed):
    terreno = TerrenoExplorable.generar_aleatorio(n, seed=seed)
    planificador = algoritmos[algoritmo](terreno)
    resultado = planificador.ejecutar()

    if resultado is None:
        return None  # No se encontró solución

    if isinstance(resultado, tuple) and len(resultado) == 4:
        d, g, E, F = resultado
    elif isinstance(resultado, tuple) and len(resultado) == 2:
        d, g = resultado
        E = len(planificador.examinados)
        F = len(planificador.frontera)
    else:
        return None

    return d, g, E, F


def ejecutar_experimentos():
    for n in tamaños:
        resultados_prom = []

        for nombre_alg in algoritmos:
            d_vals, g_vals, E_vals, F_vals = [], [], [], []

            for seed in semillas:
                resultado = resolver_mapa(n, nombre_alg, seed)
                if resultado:
                    d, g, E, F = resultado
                    d_vals.append(d)
                    g_vals.append(g)
                    E_vals.append(E)
                    F_vals.append(F)

            # Promedios
            if d_vals:  # Verifica que haya soluciones
                promedio = {
                    "algorithm": nombre_alg,
                    "d": round(sum(d_vals)/len(d_vals), 2),
                    "g": round(sum(g_vals)/len(g_vals), 2),
                    "#E": round(sum(E_vals)/len(E_vals), 2),
                    "#F": round(sum(F_vals)/len(F_vals), 2),
                }
                resultados_prom.append(promedio)

        # Guardar CSV
        ruta_csv = os.path.join(output_dir, f"{n}x{n}_resultados.csv")
        with open(ruta_csv, mode="w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["algorithm", "d", "g", "#E", "#F"])
            writer.writeheader()
            writer.writerows(resultados_prom)

        print(f"Resultados guardados en: {ruta_csv}")


if __name__ == "__main__":
    ejecutar_experimentos()
"""
from AStarSearch import BusquedaAEstrella
from BreadthFirstSearch import BusquedaAnchura
from DepthFirstSearch import BusquedaProfundidad
from Heuristicas import heuristica_euclidea
from Mapa import TerrenoExplorable
from Metricas import MetricasBusqueda


def seleccionar_algoritmo(nombre, terreno):
    if nombre == "bfs":
        return BusquedaAnchura(terreno, verbose=False)
    elif nombre == "dfs":
        return BusquedaProfundidad(terreno, verbose=False)
    elif nombre == "a*":
        return BusquedaAEstrella(
            terreno,
            heuristica=lambda p: heuristica_euclidea(p, terreno.meta),
            verbose=False,
        )
    else:
        raise ValueError(f"Algoritmo no válido: {nombre}")


def ejecutar_experimentos():
    tamanos = [3, 5, 7, 9]
    algoritmos = ["bfs", "dfs", "a*"]
    repeticiones = 10

    metricas = MetricasBusqueda()

    for tam in tamanos:
        for rep in range(repeticiones):
            terreno = TerrenoExplorable.generar_aleatorio(tam, seed=rep)

            for nombre_alg in algoritmos:
                planificador = seleccionar_algoritmo(nombre_alg, terreno)
                resultado = planificador.ejecutar()

                if isinstance(resultado, tuple) and len(resultado) == 4:
                    d, g, E, F = resultado
                elif isinstance(resultado, tuple) and len(resultado) == 2:
                    d, g = resultado
                    E = len(planificador.examinados)
                    F = len(planificador.frontera)
                else:
                    d = g = E = F = None

                metricas.registrar(
                    tamaño=tam, repetición=rep, algoritmo=nombre_alg, E=E, F=F, d=d, g=g
                )

    print("\n===== Resultados Promedio =====")
    metricas.mostrar_resultados()


if __name__ == "__main__":
    ejecutar_experimentos()
