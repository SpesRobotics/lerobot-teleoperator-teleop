from setuptools import setup, find_packages

setup(
    name="lerobot_teleoperator_teleop",
    version="0.0.1",
    description="LeRobot teleop integration",
    author="Spes Robotics",
    author_email="contact@spes.ai",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "transforms3d",
        "teleop",
        "lerobot",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
