import os
import subprocess

def main():
    print("Commandline input: ")
    while True:
        cmd = input(">")
        cmdread = subprocess.run(f"{cmd}", shell=True)
        print(f"Return {cmdread.returncode}")
        print(f"Stdout: {cmdread.stdout}")
        print(f"Check return code: {cmdread.returncode}")

if __name__ == "__main__":
    main()
