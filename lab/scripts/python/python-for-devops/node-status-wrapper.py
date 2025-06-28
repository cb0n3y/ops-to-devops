#!/usr/bin/env python3
"""
This is one of some small scripts that are made to
build skills for Python for DevOps.
"""


import shutil
from subprocess import run, PIPE


def get_node_status():
    """
    Wrappper for kubectl get nodes
    """
    # Here we pass the commands as a string because we are using shell=true
    # Only use shell=true if you are working with shell stuff heavily,
    # like piping and so on. 
    #cmd = run(['kubectl get nodes'], shell=True, check=True)
    # Here we pass the command and option as a list without shell=true
    if shutil.which('kubectl'):
        cmd = run(['kubectl', 'get', 'nodes'], check=True, stdout=PIPE, stderr=PIPE, text=True)
        print(cmd.stdout)
    else:
        print('Kubectl is not installed.')


def main():
    try:
        get_node_status()
    except CalledProcessError as e:
        print(f"[!] Command failed with code {e.returncode}: {e}")
    except FileNotFoundError:
        print("[!] kubectl not found (unexpected).")


if __name__ == '__main__':
    main()
