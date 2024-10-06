from setuptools import setup, find_packages

setup(
    name='task-cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'app': ['data/data.json'],
    },
    install_requires=[
        'python-dotenv~=1.0.1',
        'setuptools~=68.2.0',
        'pytest~=8.3.3',
    ],
    entry_points={
        'console_scripts': [
            'task-cli = main.main:main',
        ],
    },
    author="María Villascusa Marín",
    author_email="maria.villascusa@gmail.com",
    description="Una aplicación CLI para realizar tareas",
    license="MIT",
)
