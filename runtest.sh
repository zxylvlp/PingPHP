#!/bin/bash

pip install -r requirements.txt

python setup.py sdist

pip install dist/*.tar.gz

python righttest.py
