from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lerobot_teleoperator_teleop",
    version="0.0.1",
    description="LeRobot teleop integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Spes Robotics",
    author_email="contact@spes.ai",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "transforms3d",
        "teleop",
        "lerobot>=0.4",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
