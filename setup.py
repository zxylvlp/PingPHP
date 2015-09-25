from setuptools import setup
from setuptools import find_packages
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pingphp',

    version='0.0.1',

    description='A PHP code generator which use Python Like grammar',

    long_description=long_description,

    url='https://github.com/zxylvlp/PingPHP',

    author='zxylvlp',

    author_email='937141576@qq.com',

    license='MIT',

    classifiers=[

        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    # What does your project relate to?
    keywords='PHP code generator',

    packages=find_packages(exclude=['pingphp/__pycache__']),

    install_requires=['ply', 'glob2', 'watchdog'],

    entry_points={
        'console_scripts': [
            'pingrun=pingphp:run',
            'pingsee=pingphp:see',
            'pinginit=pingphp:init'
        ],
    },
)
