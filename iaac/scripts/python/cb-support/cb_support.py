"""
Write something here later.
"""


import argparse
import json
import logging
import os
import subprocess as sub
from pathlib import Path

import requests


def get_environment(envr):
    """
    Parse the option to the desire environment.
    """


def load_environment_config(env_name, service_type):
    """
    Write something here later.
    """

    config_path = Path(__file__).parent / "environments.json"
    if not config_path.exists():
        raise FileNotFoundError("environments.json not found.")

    with open(config_path, encoding="utf-8") as f:
        all_envs = json.load(f)

    if env_name not in all_envs:
        raise ValueError(f"Environment '{env_name}' not found.")

    if service_type not in all_envs[env_name]:
        raise ValueError(f"Service type '{service_type}' not defined in environment '{env_name}'.")

    return all_envs[env_name][service_type]

    # ❗ Validate upload requirement
    # if args.upload and not args.ticket:
    #     parser.error("[-] The --upload flag requires --ticket to be provided.") 

    # return args



def main():
    """
    write something here later.
    """
    parser = argparse.ArgumentParser(
        prog="cb_support.py",
        description="Gather logs from Couchbase and Sync Gateway nodes"
                    "and upload them to Couchbase support."
    )

    parser.add_argument(
        "-c", "--couchbase", action="store_true",
        help="Comma-separated list of Couchbase node IPs or hostnames."
    )
    parser.add_argument(
        "-s", "--syncgateway", action="store_true",
        help="Comma-separated list of Sync Gateway node IPs or hostnames."
    )
    parser.add_argument(
        "-e", "--environment", required=True,
        help="write somethig here later."
    )
    parser.add_argument(
        "-t", "--ticket", required=True,
        help="Couchbase support ticket ID (optional)."
    )
    parser.add_argument(
        "-u", "--upload", action="store_true",
        help="Enable automatic upload to Couchbase support."
    )
    parser.add_argument(
        "-a", "--all", action="store_true",
        help="Gather from both Couchbase and Sync Gateway."
    )

    args = parser.parse_args()

    if not any([args.couchbase, args.syncgateway, args.all]):
        parser.error("At least one of --couchbase, --syncgateway or --all must be specified.")

    if args.couchbase or args.all:
        cb_nodes = load_environment_config(args.env, "couchbase")
        print(f"[+] Gathering Couchbase logs from: {cb_nodes}")
        # add logic to download logs from cb_nodes

    if args.syncgateway or args.all:
        sgw_nodes = load_environment_config(args.env, "syncgateway")
        print(f"[+] Gathering Sync Gateway logs from: {sgw_nodes}")
        # add logic to connect to SGW nodes

    if args.couchbase:
        nodes = args.couchbase.split(',')
        print(f"[+] Collecting logs from Couchbase nodes: {nodes}")

    if args.syncgateway:
        nodes = args.syncgateway.split(',')
        print(f"[+] Collecting logs from Sync Gateway nodes: {nodes}")


if __name__ == "__main__":
    main()
