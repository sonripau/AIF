from navegacion import Navegacion
import random

class TerrenoExplorable:
    """
    Clase que representa un terreno con celdas de coste, incluyendo una posición y orientación inicial,
    y una posición y orientación objetivo.
    """

    def __init__(self, matriz, punto_inicio, ori_inicio, punto_meta, ori_meta):
        self._grilla = matriz                    # Matriz de costes del terreno
        self._inicio = punto_inicio              # Coordenadas iniciales (x, y)
        self._ori_inicio = ori_inicio            # Orientación inicial
        self._meta = punto_meta                  # Coordenadas goal (x, y)
        self._ori_meta = ori_meta                # Orientación goal

    @property
    def dimensiones(self):
        """Devuelve las dimensiones del terreno como (filas, columnas)."""
        return len(self._grilla), len(self._grilla[0]) if self._grilla else 0

    @property
    def grilla(self):
        """Devuelve la matriz de costes."""
        return self._grilla

    @property
    def inicio(self):
        """Devuelve la posición inicial."""
        return self._inicio

    @property
    def orientacion_inicio(self):
        """Devuelve la orientación inicial."""
        return self._ori_inicio

    @property
    def meta(self):
        """Devuelve la posición objetivo."""
        return self._meta

    @property
    def orientacion_meta(self):
        """Devuelve la orientación objetivo."""
        return self._ori_meta

    def costo(self, pos):
        """Devuelve el coste de moverse a una posición determinada."""
        x, y = pos
        return self._grilla[x][y]

    @classmethod
    def cargar_desde_archivo(cls, ruta):
        """
        Carga un terreno desde un archivo de texto con el siguiente formato:
        - Primera línea: número de filas y columnas
        - Luego: líneas con valores enteros para la matriz de costes
        - Penúltima línea: posición inicial + orientación (como número)
        - Última línea: posición objetivo + orientación (como número)
        """
        with open(ruta, 'r') as archivo:
            datos = [list(map(int, linea.strip().split())) for linea in archivo]

        filas, columnas = datos[0]              # Dimensiones del terreno
        grilla = datos[1:-2]                    # Matriz del terreno
        ini = tuple(datos[-2][:2])              # Coordenadas inicio
        ori_ini = Navegacion.MAPEO_ENTERO_A_DIRECCION[datos[-2][2]]  # Orientación inicio
        fin = tuple(datos[-1][:2])              # Coordenadas meta
        ori_fin = Navegacion.MAPEO_ENTERO_A_DIRECCION[datos[-1][2]]  # Orientación meta

        return cls(grilla, ini, ori_ini, fin, ori_fin)


    @staticmethod
    def generar_aleatorio(n, seed=None):
        if seed is not None:
            #random.seed(seed)
            random.seed(int(seed))  # Convierte a int siempre que no sea None

        grilla = [[0 for _ in range(n)] for _ in range(n)]

        # Colocar obstáculos aleatorios (opcional, puedes ajustar el %)
        for i in range(n):
            for j in range(n):
                if (i, j) not in [(0, 0), (n - 1, n - 1)] and random.random() < 0.2:
                    grilla[i][j] = 1  # obstáculo

        return TerrenoExplorable(
            grilla=grilla,
            inicio=(0, 0),
            meta=(n - 1, n - 1),
            orientacion_inicio='N'
        )
