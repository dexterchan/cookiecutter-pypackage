# !/usr/bin/env python
import setuptools
from distutils.core import setup
from setuptools import find_packages
import os
"""The setup script."""

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements_file_lst = ["requirements.txt"]
install_req = []
directory = os.getcwd()

for file in requirements_file_lst:
    with open(os.path.join(directory, file), "r", encoding="utf-8") as fr:
        req_texts = [n.strip() for n in fr.readlines()]
        req_texts = [t for t in req_texts if len(t) > 0]
        install_req.extend(req_texts)
test_requirements = ['pytest>=3', ]


setup(
    name='cookiecutter-pypackage',
    packages=[],
    version='0.1.0',
    description='Cookiecutter template for a Python package',
    author='Dexter Chan',
    license='BSD',
    author_email='dex@abc.com',
    url='https://github.com/audreyr/cookiecutter-pypackage',
    keywords=['cookiecutter', 'template', 'package', ],
    python_requires='>=3.7',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    test_suite='tests',
    tests_require=test_requirements,
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
