from abc import ABC, abstractmethod

class Problem(ABC):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    @abstractmethod
    def actions(self, state):
        """Return the list of actions available from a given state."""
        pass

    @abstractmethod
    def result(self, state, action):
        """Return the resulting state after applying an action."""
        pass

    def is_goal(self, state):
        return state == self.goal

    def action_cost(self, state1, action, state2):
        """Cost function used by UCS, A*, etc."""
        return 1

    def h(self, state):
        """Heuristic used by A*. Default: zero (uninformed)."""
        return 0
