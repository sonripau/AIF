from Mapa import TerrenoExplorable
from Nodo import NodoBusqueda
from BreadthFirstSearch import BusquedaAnchura
from DepthFirstSearch import BusquedaProfundidad
from AStarSearch import BusquedaAEstrella  
from Heuristicas import heuristica_euclidea
from Metricas import MetricasBusqueda

"""
This script loads a fixed map (exampleMap.txt), displays initial and goal positions,
and lets the user choose a search algorithm (BFS, DFS, or A*). It runs the selected 
search and prints out key performance metrics (depth, cost, nodes explored, frontier size).
Used for manual testing and comparison of search strategies on a known map.
"""

def mostrar_mapa_y_posiciones(terreno):
    print("\n===== Map Loaded =====")
    for fila in terreno.grilla:
        print(' '.join(str(c) for c in fila))

    filas, columnas = terreno.dimensiones
    print("\n===== Dimensions Map =====")
    print(f"Rows: {filas}, Columns: {columnas}")

    print("\n===== Positions =====")
    print(" Initial Position:", terreno.inicio, "Orientation:", terreno.orientacion_inicio)
    print(" Goal Position:", terreno.meta)

    mapa_vista = [fila.copy() for fila in terreno.grilla]
    x0, y0 = terreno.inicio
    xf, yf = terreno.meta
    mapa_vista[x0][y0] = 'S'
    mapa_vista[xf][yf] = 'G'

    print("\n===== Map with S in the Initial Position and G in Goal Position =====")
    for fila in mapa_vista:
        print(' '.join(str(c) for c in fila))

def seleccionar_algoritmo(nombre, terreno):
    nombre = nombre.lower()
    if nombre == "bfs":
        return BusquedaAnchura(terreno, verbose=True), "bfs"
    elif nombre == "dfs":
        return BusquedaProfundidad(terreno, verbose=True), "dfs"
    elif nombre == "astar" or nombre == "a*":
        #print("prueba")
        return BusquedaAEstrella(terreno, heuristica=lambda p: heuristica_euclidea(p, terreno.meta), verbose=True), "a*"
    else:
        print("Algorithm not valid. Must enter: 'bfs', 'dfs' or 'a*'")
        return None, None

def main():
    ruta_mapa = "exampleMap.txt"
    terreno = TerrenoExplorable.cargar_desde_archivo(ruta_mapa)

    mostrar_mapa_y_posiciones(terreno)

    print("\n===== Search Algorithm Selection =====")
    algoritmo = input("Enter the algorithm you want to use (bfs, dfs, a*): ")

    planificador, nombre_algo = seleccionar_algoritmo(algoritmo, terreno)
    if not planificador:
        return

    print(f"\n Executing Algorithm.... {nombre_algo.upper()}")
    resultado = planificador.ejecutar()

    # Manejo del resultado dependiendo de si incluye E y F o no
    if isinstance(resultado, tuple) and len(resultado) == 4:
        d, g, E, F = resultado
    elif isinstance(resultado, tuple) and len(resultado) == 2:
        d, g = resultado
        E = len(planificador.examinados)
        F = len(planificador.frontera)
    else:
        d = g = E = F = None
    
    metricas = MetricasBusqueda()
    metricas.registrar(tamaño=terreno.dimensiones[0], repetición=0, algoritmo=nombre_algo, E=E, F=F, d=d, g=g)
    metricas.mostrar_resultados()

if __name__ == "__main__":
    main()

