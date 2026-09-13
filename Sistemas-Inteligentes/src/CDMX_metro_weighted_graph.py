import json
import os
import googlemaps
import time
import math


def get_station_coords(graph, api_key):
    """
    Given a metro graph (dict of station -> neighbors),
    returns a dictionary mapping each station to (lat, lon)
    using Google Maps API.
    """

    gmaps_client = googlemaps.Client(key=api_key)

    coords = {}

    for station in graph.keys():
        query = f"Metro {station} CDMX"

        result = gmaps_client.find_place(
            input=query,
            input_type="textquery",
            fields=["geometry"]
        )

        candidates = result.get("candidates", [])

        if not candidates:
            print(f"[WARN] No coordinates found for {station}")
            coords[station] = None
            continue

        location = candidates[0]["geometry"]["location"]
        lat = location["lat"]
        lng = location["lng"]

        coords[station] = (lat, lng)

        # Avoid hammering the API
        time.sleep(0.2)

    return coords



def straight_line_distance(target_station, coords, method="euclidean"):
    """
    Computes straight-line (Euclidean) distance from a target station
    to all other stations in the network.

    Parameters
    ----------
    target_station : str
        The station from which distances will be computed.
    
    coords : dict
        Dictionary mapping station names to (lat, lon) or (x, y) coordinates.
        Example: {"Auditorio": (19.426, -99.191), "Polanco": (19.432, -99.197)}
    
    method : str, optional
        The method to compute distance. Currently only "euclidean" and "haversine" are supported.

    Returns
    -------
    dict
        A dictionary mapping each station to its straight-line distance
        from the target station.
    """

    if target_station not in coords:
        raise ValueError(f"Station '{target_station}' not found in coords dictionary.")

    (x1, y1) = coords[target_station]

    distances = {}

    for station, (x2, y2) in coords.items():
        # Euclidean distance
        if method == "euclidean":
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        elif method == "haversine":
            dist = haversine(y1, x1, y2, x2)
        else:
            raise ValueError("Unsupported method. Use 'euclidean' or 'haversine'.")

        distances[station] = dist

    return distances

def haversine(lat1, lon1, lat2, lon2):
    """
    Computes the great-circle distance between two points on Earth
    using the Haversine formula.

    Parameters
    ----------
    lat1, lon1 : float
        Latitude and longitude of point 1 (in decimal degrees)
    lat2, lon2 : float
        Latitude and longitude of point 2 (in decimal degrees)

    Returns
    -------
    float
        Distance in meters between the two points.
    """

    R = 6371000  # Earth radius in meters

    # Convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def gmaps_client(api_key=None):
    return googlemaps.Client(key=api_key)

def get_place_id(gmaps,station_name):
    """Busca el Place ID de una estación del metro."""
    query = f"Metro {station_name} CDMX"
    result = gmaps.find_place(
        query,
        input_type="textquery",
        fields=["place_id"]
    )
    candidates = result.get("candidates", [])
    if not candidates:
        print(f"No se encontró Place ID para {station_name}")
        return None
    return candidates[0]["place_id"]

def get_distance(gmaps, place_id_a, place_id_b):
    """Obtiene distancia en metros entre dos estaciones."""
    result = gmaps.distance_matrix(
        origins=f"place_id:{place_id_a}",
        destinations=f"place_id:{place_id_b}",
        mode="walking"
    )
    element = result["rows"][0]["elements"][0]
    if element["status"] != "OK":
        return None
    return element["distance"]["value"]  # metros

def symmetrize_distance(gmaps, pid_a, pid_b):
    d_ab = get_distance(gmaps, pid_a, pid_b)
    d_ba = get_distance(gmaps, pid_b, pid_a)

    # Si alguno falla, regresamos el otro
    if d_ab is None:
        return d_ba
    if d_ba is None:
        return d_ab

    # Usar el máximo para evitar rutas irreales
    return max(d_ab, d_ba)


def build_weighted_graph(api_key, graph):
    """Genera un grafo con pesos reales usando Google Maps."""
    place_ids = {}
    gmaps = gmaps_client(api_key)

    # Obtener Place IDs
    for station in graph:
        place_ids[station] = get_place_id(gmaps, station)
        time.sleep(0.2)

    weighted = {}

    # Obtener distancias reales simetrizadas
    for station, neighbors in graph.items():
        weighted[station] = {}
        for neighbor in neighbors:
            pid_a = place_ids[station]
            pid_b = place_ids[neighbor]

            if pid_a and pid_b:
                dist = symmetrize_distance(gmaps, pid_a, pid_b)
                weighted[station][neighbor] = dist
                time.sleep(0.2)
            else:
                weighted[station][neighbor] = None

    return weighted

# Uso:
# metro_graph = load_metro_graph()
# weighted_graph = build_weighted_graph(api_key, metro_graph)
# print(weighted_graph)
