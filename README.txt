README

# Pathfinding Search Algorithms with Orientation

This project implements classical informed and uninformed search algorithms (Breadth-First Search, Depth-First Search, and A*) over 2D grid maps. Each cell has a movement cost, and agents must navigate from a start position and orientation to a goal, optionally with a final orientation requirement.

---

## Project Overview

- Navigate 2D maps with movement and rotation.
- Compare algorithms based on cost, depth, explored nodes, and frontier size.
- Run on fixed maps or generate random maps of various sizes.
- Output experiment results in `.csv` format.

---

## File Structure

| File                      | Description |
|---------------------------|-------------|
| `main_2.py`              | Main script to run a selected algorithm on a predefined map (`exampleMap.txt`). |
| `mainMapa.py`            | Interactive script to load or generate maps. |
| `RunExperiments.py`      | Batch experiment runner with metric collection for BFS, DFS, and A*. |
| `Mapa.py`                | Terrain representation and map loader/generator. |
| `Nodo.py`                | Node structure for the search tree. |
| `Navegation.py`          | Orientation system and movement logic (N, NE, E, etc.). |
| `Heuristicas.py`         | Heuristic functions (e.g., Euclidean distance for A*). |
| `PlanificadorBase.py`    | Abstract base class defining the core logic shared across all search algorithms. |
| `BreadthFirstSearch.py`  | Implementation of BFS. |
| `DepthFirstSearch.py`    | Implementation of DFS. |
| `AStarSearch.py`         | A* implementation using Euclidean distance. |
| `Reportero.py`           | Trace and metrics printer for search results. |
| `Metricas.py`            | Class to register and compute averages across multiple runs. |
| `exampleMap.txt`         | Example map for testing. |
| `resultados_busqueda.csv`| Output from batch experiments. |

---

## Requirements

- Python 3.x
- `numpy`
- `pandas`

Install required libraries via:

```bash
pip install numpy pandas
