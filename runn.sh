#!/bin/bash
source venv/bin/activate
while true; do python3  social_app/manage.py runserver; sleep 2; done


