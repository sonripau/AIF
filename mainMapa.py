from Mapa import TerrenoExplorable

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

#"""
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