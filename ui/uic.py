#!/usr/bin/python3

import subprocess
import sys

child = subprocess.Popen(['pyuic5' ,'-x',sys.argv[1]],stdout=subprocess.PIPE)

print(str(child.communicate()[0],encoding='utf-8'))