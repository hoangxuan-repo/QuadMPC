"""Low-level joint-space PD controller."""


class JointController:
    def compute_torque(self, q, dq, q_des, dq_des):
        raise NotImplementedError
