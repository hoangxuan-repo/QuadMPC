"""MuJoCo model loading, stepping and simulation state access."""

import mujoco


class MujocoSimulator:
    def __init__(self, model_path):
        self.model = mujoco.MjModel.from_xml_path(str(model_path))
        self.data = mujoco.MjData(self.model)

    def step(self):
        mujoco.mj_step(self.model, self.data)
