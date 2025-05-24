from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''Returns requirements as a list of strings'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="MLPROJECT",
    version='0.01',
    author='Dev',
    author_email='devkumarmishra40@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

