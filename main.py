import sys

import kspdatareader

TEST_FILE = 'persistent.sfs'


def main():
    with open(TEST_FILE) as infile:
        reader = kspdatareader.KSPDataReader()
        reader.process_lines(infile.readlines())

if __name__ == '__main__':
    sys.exit(main())
