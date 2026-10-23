"""Standing simulation entry point."""

from pathlib import Path
from quad_mpc.simulation.mujoco_simulator import MujocoSimulator

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "assets" / "quadruped" / "robot.xml"


def main():
    if not MODEL.exists():
        raise FileNotFoundError(
            f"MuJoCo model not found: {MODEL}\n"
            "Add your robot MJCF model before running the simulation."
        )

    sim = MujocoSimulator(MODEL)
    print("MuJoCo model loaded.")
    print(f"Simulation timestep: {sim.model.opt.timestep}")
    # Add controller initialization and the simulation loop here.


if __name__ == "__main__":
    main()
