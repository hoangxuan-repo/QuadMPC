"""Shared data types for states, references and control commands."""

from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]


@dataclass
class RobotState:
    base_position: FloatArray
    base_quaternion: FloatArray
    base_linear_velocity: FloatArray
    base_angular_velocity: FloatArray
    joint_position: FloatArray
    joint_velocity: FloatArray
