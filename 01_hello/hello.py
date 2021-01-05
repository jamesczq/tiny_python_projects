#!/usr/bin/env python3
"""
Author: James
Purpose: Say hello with command-line arguments
"""

import argparse


def get_args():
    """Get command-line inputs"""
    parser = argparse.ArgumentParser(description='Say hello')
    # Positional arg (mandatory):
    # parser.add_argument('name', help='Name to greet')
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()


def main():
    """Main action"""
    args = get_args()
    print(f'Hello, {args.name}!')


if __name__ == '__main__':
    main()
