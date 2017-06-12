#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

setup(
    name='qt_gui_py_common',
    version='0.3.4',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Dirk Thomas',
    maintainer_email='dthomas@osrfoundation.org',
    url='https://github.com/ros2/qt_gui',
    keywords=['ROS'],
    description='qt_gui_py_common package',
    long_description=('qt_gui_py_common provides common functionality for GUI plugins written in Python.'),
    license='Apache License, Version 2.0',
)
