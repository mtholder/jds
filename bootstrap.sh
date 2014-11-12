#!/bin/sh
set -x
if ! test -d env
then
    virtualenv env | exit
fi
source env/bin/activate
pip install -r requirements.txt

echo "You will need to:"
echo "  source env/bin/activate"
