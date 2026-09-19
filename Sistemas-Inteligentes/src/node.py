class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost  # g(n)
        self.h = h                  # h(n)
        self.f = path_cost + h      # f(n)

    def path(self):
        lista_path = []
        node = self
        while node:
            lista_path.append(node.state)
            node = node.parent
        return lista_path[::-1]

    def pretty_path(self):
        camino = self.path()
        camino_str = " → ".join(camino)
        print(
            f"{camino_str}\n"
            f"Total Cost: {self.path_cost} meters"
        )

    def set_f(self, mode):
        if mode == "astar":
            self.f = self.path_cost + self.h
        elif mode == "greedy":
            self.f = self.h
        elif mode == "ucs":
            self.f = self.path_cost
        elif mode == "blind":
            self.f = 0
        else:
            raise ValueError("Unknown mode for search")

    def expand(self, problem):
        lista = []
        for action in problem.actions(self.state):
            lista.append(self.child_node(problem, action))
        return lista

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        step_cost = problem.action_cost(self.state, action, next_state)

        g = self.path_cost + step_cost
        h = problem.h(next_state)

        return Node(next_state, self, action, g, h)

    def __lt__(self, other):
        return self.f < other.f
