from dat import __version__
from setuptools import setup

long_description = ''
with open('./README.md') as f:
    long_description = f.read()

setup(name='dat',
    version=__version__,
    description='Python package for DAT Rateview http session manipulation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/christopherpryer/python-dat',
    author='Chris Pryer',
    author_email='christophpryer@gmail.com',
    license='PUBLIC',
    packages=['dat'],
    zip_safe=False)
