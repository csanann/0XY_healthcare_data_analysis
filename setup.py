#setup.py

from setuptools import setup, find_packages

setup(
    name='healthcare_data_anylysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn'
    ]
)