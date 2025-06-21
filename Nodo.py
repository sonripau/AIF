class NodoBusqueda:
    """
    Representa un nodo en el espacio de búsqueda. Contiene información sobre su posición, orientación, coste acumulado,
    profundidad, acción realizada, nodo padre y valor heurístico.
    """

    def __init__(self, pos, orient, costo_acumulado, nivel, accion_realizada="", nodo_previo=None, h_valor=0.0):
        self._pos = pos                      # Posición actual del nodo (fila, columna)
        self._orient = orient                # Orientación del robot en este nodo
        self._costo = costo_acumulado        # Coste total desde el inicio hasta este nodo 
        self._nivel = nivel                  # Profundidad (num pasos desde inicio)
        self._accion = accion_realizada      # Acción que generó este nodo
        self._padre = nodo_previo            # Nodo padre en el camino
        self._heuristica = h_valor                    # Valor heurístico (para búsqueda informada)
        self._descendientes = []             # Hijos generados desde este nodo (si se usan)

    # Propiedades de acceso
    @property
    def posicion(self): return self._pos

    @property
    def orientacion(self): return self._orient

    @property
    def coste(self): return self._costo

    @property
    def profundidad(self): return self._nivel

    @property
    def accion(self): return self._accion

    @property
    def padre(self): return self._padre

    @property
    def heuristica(self): return self._heuristica

    @property
    def hijos(self): return self._descendientes

    def __repr__(self):
        return f"Nodo(pos={self._pos}, ori='{self._orient}', coste={self._costo}, prof={self._nivel})"
