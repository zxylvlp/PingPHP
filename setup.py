from setuptools import setup

setup(
    name='PingPHP',

    version='0.0.1',

    description='A PHP code generator which use Python Like grammar',

    long_description='A PHP code generator which use Python Like grammar',

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

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: pypy',
    ],

    # What does your project relate to?
    keywords='PHP code generator',

    packages=['pingphp'],

    install_requires=['ply', 'glob2', 'watchdog'],

    entry_points={
        'console_scripts': [
            'pingrun=pingphp:run',
            'pingsee=pingphp:see'
        ],
    },
)
