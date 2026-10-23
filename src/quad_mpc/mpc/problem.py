"""Assemble the finite-horizon optimization problem."""


class MPCProblem:
    def build(self, state, reference, contacts):
        raise NotImplementedError
