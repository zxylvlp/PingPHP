from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PingPHP',

    version='0.0.1',

    description='A sample Python project',

    long_description=long_description,

    url='https://github.com/zxylvlp/PingPHP',

    author='zxylvlp',

    author_email='937141576@qq.com',

    license='MIT',

    classifiers=[

        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='PHP code generator',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['src'],


    install_requires=['ply', 'glob2', 'watchdog'],

    entry_points={
        'console_scripts': [
            'pingrun=src:run',
            'pingsee=src:see'
        ],
    },
)
