"""A simple python script template.
Processes command-line arguments for input and output files, printing these arguments to the console.
RUN: python cli_file_processor.py input.txt -o output.txt
-o output.txt: Optional argument to specify the output file. If omitted, the script will write to sys.stdout.

https://gist.github.com/nhoffman/3006600
"""

import argparse
import sys


def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
