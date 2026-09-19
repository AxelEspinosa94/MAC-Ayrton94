import json
import networkx as nx
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. Cargar líneas del metro (cada línea tiene color + network)
# ============================================================

def load_lines(path="lines.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# 2. Cargar coordenadas reales
# ============================================================

def load_coords(path="coords.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# 3. Construir grafo global + colores por línea
# ============================================================

def build_graph(graph, node_colors):
    G = nx.Graph()

    for station, neighbors in graph.items():
        for n, cost in neighbors.items():
            G.add_edge(station, n, weight=cost)

    return G, node_colors


# ============================================================
# 4. Layout geográfico usando coordenadas reales
# ============================================================

def build_geo_layout(coords):
    pos = {}
    for station, (lat, lon) in coords.items():
        pos[station] = (lon, lat)  # NetworkX usa (x=lon, y=lat)
    return pos


# ============================================================
# 5. Dibujar grafo con colores por línea
# ============================================================

def draw_metro_graph(G, pos, node_colors, output_path="output/grafo_metro.png"):
    plt.figure(figsize=(25, 25))

    # convertir colores a lista ordenada según nodos
    colors = [node_colors.get(node, "#cccccc") for node in G.nodes()]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        font_size=14,
        node_color=colors,
        edge_color="#444444"
    )

    plt.title("CDMX Metro Graph (Coordenadas Reales + Colores por Línea)", fontsize=20)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")

    print(f"✔ Imagen generada en: {output_path}")


# ============================================================
# 6. Main
# ============================================================

def main():
    print("Cargando líneas del metro...")
    lines = load_lines("lines.json")

    print("Cargando coordenadas...")
    coords = load_coords("coords.json")

    print("Construyendo grafo global...")
    G, node_colors = build_graph(lines)

    print("Construyendo layout geográfico...")
    pos = build_geo_layout(coords)

    print("Dibujando grafo...")
    draw_metro_graph(G, pos, node_colors)

    print("✔ Proceso completado.")


if __name__ == "__main__":
    main()
