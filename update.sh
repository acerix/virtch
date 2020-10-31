#!/usr/bin/env bash

pip install --upgrade pip

pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

pip freeze > requirements.txt

#yarn upgrade --latest

./collectstatic.sh

