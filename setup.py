from setuptools import setup, find_packages


setup(
    name='muv',
    version='0.0.0',
    description='View Make Up file like markdown',
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
    data_files=[('/etc/muv', ['muv/conf/muv.conf', 'muv/conf/palette.json'])]
)