from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requrement(file_path:str)-> List[str]:
    '''
    this function will return the list of requremnnts
    '''
    requrement = []
    with open(file_path) as file_obj:
        requrement = file_obj.readlines()
        [req.replace("\n","") for req in requrement]
        if HYPEN_E_DOT in requrement:
            requrement.remove(HYPEN_E_DOT)
    return requrement

setup(
name= 'MLProj',
version= '0.0.1',
author='anand',
author_email='anandsreekumar025@gmail.com',
packages= find_packages(),
install_requires =get_requrement('requrement.txt')



)