from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requires = []
    with open(file_path) as file_obj:
        requires = file_obj.readlines()
        requires = [req.replace("\n","") for req in requires]

        if HYPHEN_E_DOT in requires:
            requires.remove(HYPHEN_E_DOT)
    return requires

    
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Ayush',
    author_email = 'ayu020503@gmail.com',
    package = find_packages(),
    install_requires = get_requirements('requirements.txt')
)