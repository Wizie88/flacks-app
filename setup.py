from setuptools import setup,
find_packages

setup(
    name='app.py',
    versions='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
    ],
)