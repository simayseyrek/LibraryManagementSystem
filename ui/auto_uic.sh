#!/bin/bash

python3 uic.py LoginPage.ui -o > ../LoginPage.py
python3 uic.py RegistrationPage.ui -o > ../RegistrationPage.py
python3 uic.py BookSearch.ui -o > ../BookSearch.py