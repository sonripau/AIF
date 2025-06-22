from Mapa import TerrenoExplorable
from Mapa import mostrar_mapa_y_posiciones

"""
This script allows the user to either load a map from file or generate a random map.
It then displays the map along with the initial and goal positions. 
Useful for visual inspection and setup before running search algorithms.
"""

"""
#Prueba mapa desde archivo
def main():
    terreno = TerrenoExplorable.cargar_desde_archivo("exampleMap.txt")

    print("Map Loaded from File:")
    for fila in terreno.grilla:
        print(fila)
    print("Start:", terreno.inicio, "Orientation: " + terreno.orientacion_inicio)
    print("Goal:", terreno.meta, "Orientation: " + terreno.orientacion_meta)

if __name__ == "__main__":
    main()
"""

"""
#Prueba mapa Generado Aleatoriamente
from Mapa import TerrenoExplorable

def main():
    terreno = TerrenoExplorable.generar_aleatorio(5, seed=42)

    print("Random Map generated:")
    for fila in terreno.grilla:
        print(fila)
    print("Start:", terreno.inicio, "Orientation: " + str(terreno.orientacion_inicio))
    print("Goal:", terreno.meta, "Orientation: " + str(terreno.orientacion_meta))

if __name__ == "__main__":
    main()
#"""

# Interactive menu for the user to choose between loading a map or generating a random one
def main():
    print("¿Which type of map do you want to use?")
    print("1. Load map from file")
    print("2. Generate a random map nxn")
    opcion = input("Choose an option (1 o 2): ")

    if opcion == "1":
        ruta = input("Enter the name of the file (default: exampleMap.txt): ")
        if not ruta.strip():
            ruta = "exampleMap.txt"
        terreno = TerrenoExplorable.cargar_desde_archivo(ruta)
    elif opcion == "2":
        tam = input("Size of the map (ex. 5): ")
        seed = input("Seed for randomness (optional): ")
        tam = int(tam)
        seed = int(seed) if seed.strip() else None
        terreno = TerrenoExplorable.generar_aleatorio(tam, seed=seed)
    else:
        print("Option no valid.")
        return

    mostrar_mapa_y_posiciones(terreno)

if __name__ == "__main__":
    main()
