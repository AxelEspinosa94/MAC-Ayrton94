import json
import os

def load_metro_graph(folder="metro"):
    graph = {}

    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Fusionar diccionarios
            for station, neighbors in data.items():
                if station not in graph:
                    graph[station] = {}

                for n, cost in neighbors.items():
                    graph[station][n] = cost  # peso (1 por ahora)

    print(f"{len(graph)} stations were uploaded from '{folder}' directory.")
    return graph
