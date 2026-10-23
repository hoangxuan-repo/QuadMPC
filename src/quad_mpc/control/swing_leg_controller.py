"""Swing-leg tracking controller."""


class SwingLegController:
    def compute_torque(self, state, foot_reference):
        raise NotImplementedError
