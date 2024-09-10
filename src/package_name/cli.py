"""
Command line interface for package_name
"""

import argparse
from . import core

# useful for debugging
# from ipydex import IPS, activate_ips_on_exception
# activate_ips_on_exception()


def main():

    # docs: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help=f"main command", default=None)

    args = parser.parse_args()

    if args.cmd:
        print("command: ", cmd)
        core.main()
    else:
        print("nothing to do, see option `--help` for more info")
