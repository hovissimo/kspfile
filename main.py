import sys

TEST_FILE = 'persistent.sfs'


def main():
    with open(TEST_FILE) as infile:
        lines = infile.readlines()

if __name__ == '__main__':
    sys.exit(main())
