import subprocess
import sys
import os

def run_login():
    os.environ["RUNNING_FROM_MAIN"] = "true"
    subprocess.Popen([sys.executable, "src/login.py"])

if __name__ == "__main__":
    run_login()
