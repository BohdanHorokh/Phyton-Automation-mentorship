from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='basic pytest project',
    version='0.1.0',
    description='Mentorship project',
    long_description=readme,
    author='Bogdan Gorokh',
    author_email='bogdan.gorokh@gmail.com',
    packages=find_packages('tests'),
    install_requires=[
        'pytest',
        'selenium'
    ],
)
