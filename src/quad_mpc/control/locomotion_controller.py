"""Coordinate state, gait, MPC and leg control."""


class LocomotionController:
    def compute_control(self, state, reference, contacts):
        raise NotImplementedError
