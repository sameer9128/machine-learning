from setuptools import find_packages,setup


from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path)->List[str]:
    '''
    thisfunction will return the list of requirements
    '''
    rerquirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
             requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='krish',
    author_email='ahmadsameer7992@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
    
    
    
       
    