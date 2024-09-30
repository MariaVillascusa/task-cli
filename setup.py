from setuptools import setup, find_packages

setup(
    name='task_traker_cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mi_comando=mi_proyecto.cli:main',  # Define el comando principal
        ],
    },
)