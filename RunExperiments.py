import csv
import os
import random
import pandas as pd
import numpy as np

from AStarSearch import BusquedaAEstrella
from BreadthFirstSearch import BusquedaAnchura
from DepthFirstSearch import BusquedaProfundidad
from Heuristicas import heuristica_euclidea
from Mapa import TerrenoExplorable
from Metricas import MetricasBusqueda

# This script runs a batch of search experiments (BFS, DFS, A*) on randomly generated maps 
# of various sizes (3x3, 5x5, 7x7, 9x9). For each configuration, it executes 10 repetitions 
# and records performance metrics such as number of expanded nodes (E), final frontier size (F), 
# path depth (d), and total cost (g). Results are saved to a CSV file for further analysis.

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
    resultados_lista = []

    for tam in tamanos:
        for rep in range(repeticiones):
            terreno = TerrenoExplorable.generar_aleatorio(tam, seed=rep)

      # Guardar el mapa
            os.makedirs("mapas_generados", exist_ok=True)
            terreno.guardar_en_archivo(f"mapas_generados/mapa_{tam}x{tam}_rep{rep}.txt")

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
                resultados_lista.append({
                    "map_size": tam,
                    "repetition": rep,
                    "algorithm": nombre_alg,
                    "E": E,
                    "F": F,
                    "d": d,
                    "g": g
                })

    print("\n===== Average Results =====")
    metricas.mostrar_resultados()
    # Guardar resultados a CSV
    df = pd.DataFrame(resultados_lista)
    df.to_csv("resultados_busqueda.csv", index=False)


if __name__ == "__main__":
    ejecutar_experimentos()
