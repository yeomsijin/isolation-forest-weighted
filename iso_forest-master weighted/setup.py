import sys
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
prjdir = os.path.dirname(__file__)

def read(filename):
    return open(os.path.join(prjdir, filename)).read()

extra_link_args = []
libraries = []
library_dirs = []
include_dirs = []
exec(open('version.py').read())
setup(
    name='iso_forest',
    version=__version__,
    author='Matias Carrasco Kind',
    author_email='mcarras2@illinois.edu',
    scripts=[],
    py_modules=['iso_forest','version'],
    packages=[],
    license='License.txt',
    description='Isolation Forest for anomaly detection',
    long_description=read('README.md'),
    url='https://github.com/mgckind/iso_forest',
    install_requires=["numpy"],
)
