import os
import subprocess

print("Commandline input: ")
while True:
    cmd = input(">")
    cmdread = subprocess.run(f"{cmd}", shell=True)
    print(cmdread.stdout)
