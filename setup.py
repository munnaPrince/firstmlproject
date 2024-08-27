from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this function returns the list of requirements
    '''

    HYPEN_DOT ='-e .'
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPEN_DOT in requirements:
        requirements.remove(HYPEN_DOT)

    return requirements

setup(
name="mlproject",
version='0.0.1',
author="Munnaf",
author_email="munnaf.prince.48@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")


)