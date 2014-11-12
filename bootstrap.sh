#!/bin/bash
set -x
if ! test -d env
then
    virtualenv env || exit
fi
. env/bin/activate || exit
pip install -r requirements.txt

echo "You will need to:"
echo "  . env/bin/activate"
