from setuptools import setup, find_packages
from typing import List

HYEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements file and return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[requirement.replace("\n","") for requirement in requirements]
        if HYEN_E_DOT in requirements:
            requirements.remove(HYEN_E_DOT)

    return requirements

setup(
   name='ML_learn',
   version='0.0.1',
   description='A useful module',
   author='Doulakhom',
   author_email='doulakhomtps11@gmail.com',
   packages=find_packages(),  #same as name
   install_requires= get_requirements('requirements.txt'), #external packages as dependencies
   include_package_data=True,
)