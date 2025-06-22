import math

def heuristica_euclidea(pos_actual, pos_objetivo):
    """
    Computes the Euclidean distance between the current position and the goal position.
    This heuristic is used in A* search to estimate the cost-to-go from a given node.
    It assumes movement in any direction (including diagonals) is possible and ignores obstacles.

    Parameters:
        pos_actual (tuple): The current position (x, y).
        pos_objetivo (tuple): The goal position (x, y).

    Returns:
        float: The straight-line (Euclidean) distance between the two points.
    """
    x1, y1 = pos_actual
    x2, y2 = pos_objetivo
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
