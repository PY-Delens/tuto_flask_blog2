#!/usr/bin/bash
# running it : $ ./cabwill_1.sh
# oneline comment
<<COMMENT
    This is a multiple line comment
    In Bash Scripting
COMMENT
echo Good Day!
# poetry shell  # doesn't work in bash file
export FLASK_ENV=development
export FLASK_APP=cabwill_1.py
#	flask run
poetry run flask run

