#!/usr/bin/python3

import subprocess
import sys

child = subprocess.Popen(['pyuic5' ,'-x',sys.argv[1]],stdout=subprocess.PIPE)

print(str(child.communicate()[0],encoding='utf-8'))

# python3 uic.py LoginPage.ui -o > ../LoginPage.py
# python3 uic.py RegistrationPage.ui -o > ../RegistrationPage.py
# python3 uic.py BookSearch.ui -o > ../BookSearch.py
