from subprocess import Popen, PIPE

program = 'python sample.py'
proc = Popen("python sample.py", stdout=PIPE, bufsize=1)

for line in iter(proc.stdout.readline, b''):
    print(line)
proc.stdout.close()
proc.wait()