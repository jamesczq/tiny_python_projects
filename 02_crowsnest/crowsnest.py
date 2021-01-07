#!/usr/bin/env python3
"""
Author : jamesczq <jamesczq@localhost>
Date   : 2021-01-06
Purpose: Provide correct article (a/an) for a noun
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
