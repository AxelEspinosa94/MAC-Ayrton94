import heapq
from collections import deque

from src.node import Node


def depth_first_graph_search(problem):
    start_node = Node(problem.initial)
    if problem.is_goal(start_node.state):
        return start_node
    frontier = [start_node]
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node.state)

        if problem.is_goal(node.state):
            return node

        for child in node.expand(problem):
            if child.state not in explored:
                frontier.append(child)

    return None

def breadth_first_graph_search(problem):
    start_node = Node(problem.initial)
    if problem.is_goal(start_node.state):
        return start_node
    frontier = deque([start_node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)

        if problem.is_goal(node.state):
            return node

        for child in node.expand(problem):
            if child.state not in explored:
                frontier.append(child)

    return None

def search_informed(problem, mode="astar"):
    start = Node(
        state=problem.initial,
        parent=None,
        action=None,
        path_cost=0,
        h=problem.h(problem.initial)
    )
    start.set_f(mode)

    frontier = []
    heapq.heappush(frontier, start)

    explored = {}

    while frontier:
        node = heapq.heappop(frontier)

        if problem.is_goal(node.state):
            return node

        if node.state in explored and explored[node.state] <= node.path_cost:
            continue

        explored[node.state] = node.path_cost

        for child in node.expand(problem):
            child.set_f(mode)

            if child.state in explored and explored[child.state] <= child.path_cost:
                continue

            heapq.heappush(frontier, child)

    return None

def hill_climbing(problem):
    # Nodo inicial
    current = Node(
        state=problem.initial,
        parent=None,
        action=None,
        path_cost=0,
        h=problem.h(problem.initial)
    )

    while True:
        # Expandir vecinos
        neighbors = current.expand(problem)

        if not neighbors:
            return current  # sin vecinos → atasco

        # Elegir el vecino con mejor heurística (menor h)
        next_node = min(neighbors, key=lambda n: n.h)

        # Si no mejora, estamos en un máximo local
        if next_node.h >= current.h:
            return current

        # Avanzar
        next_node.parent = current
        current = next_node
