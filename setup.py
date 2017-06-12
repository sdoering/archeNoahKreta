import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bentham",
    description="Tool for monitoring online performance metrics and generating optimization tipps.",
    author="Sven 'sdoering' Doering",
    packages=find_packages(exclude=['data', 'figures', 'output', 'notebooks']),
    long_description=read('README.md'),
)
