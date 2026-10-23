"""State estimation interface."""


class StateEstimator:
    def update(self, measurements):
        raise NotImplementedError
