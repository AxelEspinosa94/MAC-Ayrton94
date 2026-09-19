from src.Problem import Problem

class GraphProblem(Problem):
    def __init__(self, initial, goal, graph, heuristic_table=None):
        super().__init__(initial, goal)
        self.graph = graph
        self.heuristic_table = heuristic_table or {}

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def action_cost(self, state1, action, state2):
        # DFS/BFS ignoran esto
        return self.graph[state1][state2]

    def h(self, state):
        # DFS/BFS ignoran esto
        return self.heuristic_table.get(state, 0)
