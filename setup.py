#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@todo:
 - Figure out how to properly handle install_requires for things which don't
   always install the requisite metadata for normal detection.
"""

try:
    from setuptools import setup
except ImportError:
    # TODO: Verify that this branch actually works
    from distutils.core import setup

    from ez_setup import use_setuptools
    use_setuptools()

REQUIRES = []

# Detect PyGTK without requiring egg metadata
try:
    # pylint: disable=unused-import
    import gobject  # NOQA
except ImportError:
    REQUIRES.append('pygtk')

# Detect dbus-python without requiring egg metadata
try:
    # pylint: disable=unused-import
    import dbus  # NOQA
except ImportError:
    REQUIRES.append('dbus-python')

# Detect PyNotify without requiring egg metadata and support notify2 as well
try:
    # pylint: disable=unused-import
    import notify2  # NOQA
except ImportError:
    try:
        # pylint: disable=unused-import
        import pynotify  # NOQA
    except ImportError:
        REQUIRES.append('notify2')

# Detect VTE without requiring egg metadata
try:
    # pylint: disable=unused-import
    import vte  # NOQA
except ImportError:
    print("Your system lacks the Python bindings for libvte (python-vte) "
          "but they cannot be automatically installed by this script. "
          "Aborting.")
    import sys
    sys.exit(1)

# Try to get the version from the program itself
# TODO: Decide on a more proper way to dedupe the version number
try:
    from lgogd_uri import __version__ as version
except BaseException:
    version = None

setup(
    name="lgogd_uri",
    version=version,
    description="Frontend to enable gogdownloader:// URLs in lgogdownloader",
    author="Stephan Sokolow (detarion/SSokolow)",
    author_email="http://www.ssokolow.com/ContactMe",
    # url = "http://ssokolow.github.com/lgogd_uri/",

    license="License :: OSI Approved :: MIT License",
    # TODO: Trove Classifiers
    install_requires=REQUIRES,

    packages=['lgogd_uri'],
    package_data={'lgogd_uri': ['*.glade', '*.png']},
    data_files=[('share/applications', ['lgogd_uri.desktop'])],
    entry_points={'gui_scripts': ['lgogd_uri = lgogd_uri.main:main']}
)

# vim: set sw=4 sts=4 expandtab :