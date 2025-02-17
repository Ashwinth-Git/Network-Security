from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads requirements from requirements.txt and returns them as a list.
    Returns:
        List[str]: List of required package names
    """
    requirement_list: List[str] = []
    
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Skip empty lines and -e . (editable install)
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
                    
    except FileNotFoundError:
        print("Warning: requirements.txt file not found")
    except Exception as e:
        print(f"Error reading requirements.txt: {str(e)}")
        
    return requirement_list

setup(
    name="Network Security",
    version="0.0.5",
    author="Ashwinth Ragu",
    author_email="ashwinth.ragu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)