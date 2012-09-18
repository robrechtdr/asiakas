#from distutils.core import setup
from setuptools import setup

setup(
    name='Asiakas',
    author='Robrecht De Rouck',
    author_email='Robrecht.De.Rouck@gmail.com',
    py_modules=['asiakas'],
    entry_points={
    'console_scripts': ['asiakas = asiakas:main', ],},
    description='A tiny python text-based web browser.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests>=0.13.2", "html2text>=3.200.3", "pyfiglet"
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
)

#entry_points="""[console_scripts]pykaboo = pykaboo:main"""
