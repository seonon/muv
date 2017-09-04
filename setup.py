"""Package setup"""
import os
from os.path import expanduser

from setuptools import find_packages, setup

from muv import __version__

exec(open(os.path.join("muv", "version.py")).read())

setup(
    name='muv',
    version=__version__,
    description='View markdown file in command line',
    long_description='View markdown file in command line',
    url='https://github.com/seonon/muv',
    author='seonon',
    author_email='nanttery@gmail.com',
    license='GNU GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing :: Markup',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='markdown file preview',
    packages=find_packages(),
    install_requires=["markdown", "urwid", "py-gfm", "beautifulsoup4"],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'muv=muv:main',
        ],
    },
    data_files=[(expanduser('~/.muv'), ['muv/conf/muv.conf', 'muv/conf/palette.json', 'muv/conf/palette_without_italics.json'])],
    include_package_data=True
)
