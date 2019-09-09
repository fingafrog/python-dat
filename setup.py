
from setuptools import setup

long_description = ''
with open('./README.md') as f:
    long_description = f.read()

setup(name='dat',
    version='0.1',
    description='Python package for Dat Rateview http session manipulation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NFI-Solutions-Engineering/dat',
    author='Chris Pryer',
    author_email='chris.pryer@nfiindustries.com',
    license='PRIVATE',
    packages=['dat'],
    zip_safe=False)
