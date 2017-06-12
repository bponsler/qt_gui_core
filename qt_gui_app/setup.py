#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

setup(
    name='qt_gui_app',
    version='0.3.4',
    packages=[],
    package_dir={},
    scripts=['scripts/qt_gui_app'],
    install_requires=['setuptools'],
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Dirk Thomas',
    maintainer_email='dthomas@osrfoundation.org',
    url='https://github.com/ros2/qt_gui',
    keywords=['ROS'],
    description='qt_gui_app package',
    long_description=(
        'qt_gui_app provides the main to start an instance of the integrated graphical user interface provided by qt_gui.'),
    license='Apache License, Version 2.0',
)
