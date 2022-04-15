import os
import subprocess
import re
from sys import stdout 

def proc_input(inp, arr):
    tpm = inp
    x = tpm.split(' ')
    for i in x:
        arr.append(i)
    return arr


def main():
    while True:
        tpmArr = []
        cmd = input(">")
        proc_input(cmd, tpmArr)
        cmdread = subprocess.run(proc_input(cmd, tpmArr), shell=True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Return {cmdread.returncode}")
        print(f"Stdout: {cmdread.stdout}")
        print(f"Check return code: {cmdread.returncode}")
        print(cmdread.stdout.decode("utf-8"))
        

if __name__ == "__main__":
    main()
