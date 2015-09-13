#!/bin/bash

pip install -r requirements.txt

python setup.py sdist

twine upload dist/*.tar.gz
