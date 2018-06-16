#!/bin/sh
rm -r lh-py3env
#virtualenv --distribute -p python3 reiseEnv
python3 -m venv lh-py3env
lh-py3env/bin/pip install -r requirements.txt
echo "run 'source lh-py3nv/bin/activate' to use this environment"
