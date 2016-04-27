import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

VERSION = (0, 0, 1)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]

version = str_version

setup(
    name='pyfka',
    version=version,
    description="Another python kafka client.",
    long_description="",
    author='Jakub Racek',
    author_email='me@jakubracek.net',
    url='https://github.com/jacobjakub/pyfka',
    license='Apache Software License (v2)',
    install_requires=[
        'kafka-python >=1.1.1',
    ],
    setup_requires=[],
    test_suite='pyfka.collector',
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
    }
)
