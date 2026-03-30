from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_list


setup(
    name="AI-TRAVEL-PLANNER",
    version="0.1.0",
    author="Gowtham K B",
    author_email="gowthamkb2002@gmail.com",
    description="An Agentic AI Trip Planner application",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=get_requirements()
)
