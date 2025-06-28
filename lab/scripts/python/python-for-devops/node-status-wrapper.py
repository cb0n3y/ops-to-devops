#!/usr/bin/env python3
"""
This is one of some small scripts that are made to
build skills for Python for DevOps.
"""


import shutil
from subprocess import run, PIPE, CalledProcessError


def get_node_status():
    """
    Wrappper for kubectl get nodes
    """
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
