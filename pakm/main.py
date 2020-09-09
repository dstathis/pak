import argparse
import os
import subprocess

from pakm import constants


def run(cmd):
    subprocess.run(cmd.split(), check=True)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=[x for x in constants.cmds])
    parser.add_argument('pkgs', nargs='*')
    return parser.parse_args()


def main():
    with open('/etc/os-release') as f:
        for line in f.read().splitlines():
            key, value = line.split('=')
            os.environ[key] = value

    args = parse_args()

    pkg_man = constants.os_ids[os.environ['ID']]
    if callable(pkg_man):
        pkg_man = pkg_man()

    cmd_strs = []
    for cmd_template in constants.cmds[args.action][pkg_man]:
        cmd_strs.append(cmd_template.format(' '.join(args.pkgs)))
    for cmd_str in cmd_strs:
        run(cmd_str)


if __name__ == '__main__':
    main()
