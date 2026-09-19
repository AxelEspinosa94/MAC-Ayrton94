import json
import os

def load_metro_graph(folder="../metro"):
    graph = {}
    node_colors = {}

    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            color = data.get("color", "#cccccc")  # color de la línea
            network = data.get("network", {})

            # Fusionar diccionarios
            for station, neighbors in network.items():
                # asignar color a la estación
                node_colors[station] = color

                if station not in graph:
                    graph[station] = {}

                for n, cost in neighbors.items():
                    graph[station][n] = cost

    print(f"{len(graph)} stations were uploaded from '{folder}' directory.")
    return graph, node_colors
