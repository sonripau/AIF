import math

def heuristica_euclidea(pos_actual, pos_objetivo):
    x1, y1 = pos_actual
    x2, y2 = pos_objetivo
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
