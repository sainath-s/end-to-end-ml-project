from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    '''
        This function will return the list of packages
    '''
    requirements=[]
    with open(file=file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    description='End-to-End-ML Project',
    author='Sainath S',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)