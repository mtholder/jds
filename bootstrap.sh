#!/bin/bash
set -x
if ! test -d env
then
    virtualenv env || exit
fi
. env/bin/activate || exit
pip install -r requirements.txt || exit
cd jds 
python setup.py develop || exit

echo "You will need to:"
echo "  . env/bin/activate"
echo "and then run:"
echo "  pserve development.ini --reload"
echo "from $PWD to run the server in debug mode (not safe for deployment)."
