'''
The setup.py file is used to package the project as a Python package.
It includes metadata about the package, such as its name, version, author,and more.
It also specifies the dependencies required to run the package and the entry points for command-line interfaces.
'''

from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    Returns:
        List[str]: A list of dependencies.
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                requirements = line.strip()
                ## Ignore empty lines and -e . 
                if requirements and requirements != '-e .':
                    requirement_list.append(requirements)
           
    except FileNotFoundError:
        print("requirements.txt file not found. Please make sure it exists in the project directory.")

    return requirement_list

## print(get_requirements())

### Setup function to package the project Metadata and dependencies ###
setup(
    name="NetWork Security",
    version="0.0.1",
    author="Abeshith",
    author_email="abeshith24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)