# Executing cli commands from python script
import subprocess

cmd = ["ls", "-lh"]
cmd_run = subprocess.run(cmd, capture_output=True)

for thing in cmd_run.stdout.decode().split('\n'):
    print(thing)
