import sys, random, subprocess
from subprocess import Popen, PIPE

program = 'python sample.py'
proc = subprocess.Popen("python sample.py", stdout=subprocess.PIPE, bufsize=1)

for line in iter(proc.stdout.readline, b''):
    print(line)
proc.stdout.close()
proc.wait()