class Navegacion:
    """
    Clase utilitaria que define las direcciones posibles de movimiento,
    los vectores de desplazamiento asociados a cada dirección,
    y funciones para avanzar en el terreno según una orientación.
    """

    # Lista de direcciones principales (en sentido horario)
    DIRECCIONES = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "--"]

    # Direcciones incluyendo la opción de quedarse quieto ("I" de Idle)
    CON_IDLE = DIRECCIONES + ["I"]

    # Vectores de desplazamiento asociados a cada dirección
    MOVIMIENTOS = {
        "N": (-1, 0),  # Arriba
        "NE": (-1, 1),  # Arriba-derecha
        "E": (0, 1),  # Derecha
        "SE": (1, 1),  # Abajo-derecha
        "S": (1, 0),  # Abajo
        "SW": (1, -1),  # Abajo-izquierda
        "W": (0, -1),  # Izquierda
        "NW": (-1, -1),  # Arriba-izquierda
    }

    # Mapeo de números enteros a direcciones, útil al leer desde archivo
    MAPEO_ENTERO_A_DIRECCION = {
        0: "N",
        1: "NE",
        2: "E",
        3: "SE",
        4: "S",
        5: "SW",
        6: "W",
        7: "NW",
        8: "I",  # Idle
    }

    @staticmethod
    def avanzar(orientacion, desde):
        """
        Devuelve la nueva posición al avanzar una celda en la dirección indicada.
        :param orientacion: dirección a seguir
        :param desde: posición actual (x, y)
        :return: nueva posición (x, y)
        """
        dx, dy = Navegacion.MOV[orientacion]
        return (desde[0] + dx, desde[1] + dy)


# Variables de acceso rápido para otros módulos
DIRECTIONS = Navegacion.DIRECCIONES
MOVES = Navegacion.MOVIMIENTOS
