#!/usr/bin/env python3
"""
The program allows user to convert numbers between bases from 2 to 36 by
extending the available characters' set to all 26 letters of English alphabet
10 digits + 26 letters = 36 characters
"""
import argparse

__author__ = "Matt23"
__copyright__ = "Copyright 2016"
__license__ = "MIT"


def main():
    arg_parser = argparse.ArgumentParser(description="Converting numbers between bases")
    arg_parser.add_argument('number', type=str.upper, help='the number supposed to be converted')
    arg_parser.add_argument('current_base', type=int, help='base the number is written in')
    arg_parser.add_argument('new_base', type=int, help='base the number will be converted to')
    arg_parser.add_argument('-r', '--raw', action='store_true', help='displays the converted number only')
    arg_parser.add_argument('-c', '--count', action='store_true', help='counts characters in output')
    arg_parser.add_argument('-l', '--length', type=int,
                            help='appends preceding zeros if output is shorter than given number', default=0)
    args = arg_parser.parse_args()

    try:
        number = convert_number_to_base(args.number, args.current_base, args.new_base)
    except Exception as e:
        print(e)
        return

    # appends preceding zeros to output if requested
    if args.length > len(number):
        count = args.length - len(number)
        number = '0' * count + number

    output = number

    # adds extended output unless --raw specified
    if not args.raw:
        output = "{}({}) = {}({})".format(args.number, args.current_base, number, args.new_base)


    # adds number's length to the output if --count specified  
    if args.count:
        output += "  # {} characters".format(len(number))

    print(output)


def convert_number_to_base(number, current_base, new_base):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # characters the value can be written with
    decimal_representation = 0

    # checking whether given bases are valid
    if current_base not in range(2, len(characters) + 1) or new_base not in range(2, len(characters) + 1):
        raise Exception("The base must be in range from 2 to {}".format(len(characters)))

    # converting value to 10 based system and checking its correctness
    for exponent, c in enumerate(number[::-1]):  # enumerating reverted string
        if characters.index(c) >= current_base:
            raise Exception("The number is not written in {} based system".format(current_base))
        decimal_representation += characters.index(c) * current_base ** exponent

    # converting number to requested base by doing modulo calculations
    requested_representation = ""
    while decimal_representation >= 1:
        requested_representation += characters[decimal_representation % new_base]
        decimal_representation //= new_base

    return requested_representation[::-1]


if __name__ == '__main__':
    main()
