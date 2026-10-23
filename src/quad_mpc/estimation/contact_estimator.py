"""Foot contact estimation interface."""


class ContactEstimator:
    def update(self, measurements):
        raise NotImplementedError
