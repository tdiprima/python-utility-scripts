# Allows printing of messages to the standard error output.
from __future__ import print_function

import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("some message", 1)
