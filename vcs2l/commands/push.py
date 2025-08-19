import argparse
import sys

from vcs2l.commands.command import Command, simple_main
from vcs2l.streams import set_streams


class PushCommand(Command):
    command = 'push'
    help = 'Push changes from the working copy to the repository'

    def __init__(self, args):
        super(PushCommand, self).__init__(args)


def get_parser():
    parser = argparse.ArgumentParser(
        description='Push changes from the working copy to the repository',
        prog='vcs push',
    )
    parser.add_argument_group('"push" command parameters')
    return parser


def main(args=None, stdout=None, stderr=None):
    set_streams(stdout=stdout, stderr=stderr)
    parser = get_parser()
    return simple_main(parser, PushCommand, args)


if __name__ == '__main__':
    sys.exit(main())
