from Mapa import TerrenoExplorable
from Nodo import NodoBusqueda
from BreadthFirstSearch import BusquedaAnchura
from DepthFirstSearch import BusquedaProfundidad
from AStarSearch import BusquedaAEstrella  
from Heuristicas import heuristica_euclidea
from Metricas import MetricasBusqueda

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

    print(f"\n>>> Executing Algorithm.... {nombre_algo.upper()}")
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
    """
    if resultado is None:
        print("Not found path.")
        return

    if isinstance(resultado, tuple):
        d, g = resultado
    else:
        d = g = None

    # Métricas
    E = len(planificador.examinados) 
    F = len(planificador.frontera)
    """
    
    metricas = MetricasBusqueda()
    metricas.registrar(tamaño=terreno.dimensiones[0], repetición=0, algoritmo=nombre_algo, E=E, F=F, d=d, g=g)
    metricas.mostrar_resultados()

if __name__ == "__main__":
    main()


"""
# === Cargar el archivo de mapa ===
ruta_mapa = "exampleMap.txt"
terreno = TerrenoExplorable.cargar_desde_archivo(ruta_mapa)

# === Mostrar mapa y posiciones ===
print("\n===== Map Loaded =====")
for fila in terreno.grilla:
    print(' '.join(str(c) for c in fila))

print("\n===== Dimensions Map =====")
filas, columnas = terreno.dimensiones
print(f"Rows: {filas}, Columns: {columnas}")

print("\n===== Positions =====")
print(" Initial Position:", terreno.inicio, "Orientation:", terreno.orientacion_inicio)
print(" Goal Position:", terreno.meta)

# mark initial/goal positions with S and G
mapa_vista = [fila.copy() for fila in terreno.grilla]
x0, y0 = terreno.inicio
xf, yf = terreno.meta
mapa_vista[x0][y0] = 'S'
mapa_vista[xf][yf] = 'G'

print("\n===== Map with S in the Initial Position and G in Goal Position =====")
for fila in mapa_vista:
    print(' '.join(str(c) for c in fila))

print("\n===== Search Algorithm =====")
# === Elegir el algoritmo ===
planificador = BusquedaAnchura(terreno, verbose=True)

# === Ejecutar algoritmo y recolectar métricas ===
resultado = planificador.ejecutar()
# Recuperar d y g del resultado original
d, g = resultado

# Calcular E y F desde los atributos del planificador
E = len(planificador.examinados)
F = len(planificador.frontera)

# === Registrar y mostrar métricas ===
metricas = MetricasBusqueda()
metricas.registrar(tamaño=terreno.dimensiones[0], repetición=0, algoritmo="bfs", E=E, F=F, d=d, g=g)
metricas.mostrar_resultados()

from DepthFirstSearch import BusquedaProfundidad  # si lo llamas así

planificador = BusquedaProfundidad(terreno, verbose=True)
d, g, camino = planificador.ejecutar()
planificador.reportero.mostrar_mapa_con_camino(terreno, camino)
"""