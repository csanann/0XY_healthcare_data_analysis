#setup.py

from setuptools import setup, find_packages

setup(
    name='healthcare_data_anylysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'matplotlib>=3.0.0',
        'scikit-learn>1.0.0',
        'Flask>1.1.4',
        'Werkzeug>=2.0.0,<2.1.0'
    ]
)