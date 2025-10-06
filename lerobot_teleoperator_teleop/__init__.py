from dataclasses import dataclass

from lerobot.teleoperators.config import TeleoperatorConfig


@TeleoperatorConfig.register_subclass("lerobot_teleoperator_teleop")
@dataclass
class TeleopConfig(TeleoperatorConfig):
    port: str = "4443"
    host: str = "0.0.0.0"
    use_gripper: bool = True
    device_class: str = "lerobot_teleoperator_teleop.teleop.LeTeleop"
