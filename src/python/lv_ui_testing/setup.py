from setuptools import setup, find_packages
setup(
name='lv-ui-testing',
version='0.1.0',
author='Thomas Zilliox',
author_email='thomas.zilliox67@gmail.com',
description='A LabVIEW User Interface Testing framework.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)