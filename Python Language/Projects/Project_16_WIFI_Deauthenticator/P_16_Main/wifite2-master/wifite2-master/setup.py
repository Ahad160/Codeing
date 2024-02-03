#!/usr/bin/env python

try:
    from setuptools import setup
except:
    raise ImportError("setuptools is required to install defite2")

from defite.config import Configuration

setup(
    name='defite',
    version=Configuration.version,
    author='kimocoder',
    author_email='christian@aircrack-ng.org',
    url='https://github.com/kimocoder/defite2',
    packages=[
        'defite',
        'defite/attack',
        'defite/model',
        'defite/tools',
        'defite/util',
    ],
    data_files=[
        ('share/dict', ['wordlist-probable.txt'])
    ],
    license='GNU GPLv2',
    scripts=['bin/defite'],
    description='Wireless Network Auditor for Linux & Android',
    # long_description=open('README.md').read(),
    long_description='''Wireless Network Auditor for Linux & Android.

    Sniff, Injects and Cracks WEP, WPA/2, and WPS encrypted networks.

    Depends on Aircrack-ng Suite, Tshark (from Wireshark),
    and various other external tools.''',

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ]
)
