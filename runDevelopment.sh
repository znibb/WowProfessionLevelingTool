#!/bin/bash

if [[ -f venv/bin/activate ]]; then
  echo "Activating virtualenv"
  source venv/bin/activate
else
  echo "Creating virtualenv"
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
fi

export FLASK_ENV=development
export SECRET_KEY=thisdoesntreallymatter

echo "Starting Flask"
flask run
