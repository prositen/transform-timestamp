#!/usr/bin/env python3
import argparse
import csv
import datetime
import fileinput
import sys
__author__ = 'anna'

"""
This tool reads a CSV where one field contains a Unix timestamp, and writes a CSV where this field is
replaced with a date-time on ISO-8601 format
"""


class Parser(object):
    def __init__(self, args):
        parser = self.get_arg_parser()
        self.args = parser.parse_args(args)

    @staticmethod
    def get_arg_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('-k', '--key',
                            help='Key column',
                            type=int)
        parser.add_argument('-t', '--delimiter',
                            help='Delimiter',
                            default=',')
        parser.add_argument('--file', help='File', nargs='*', default='-')
        parser.add_argument('--timestamp_read',
                            help="C standard datetime formats. Default is unix timestamp",
                            default=None)
        parser.add_argument('--timestamp_write',
                            help="C standard datetime formats. Default is ISO-8601",
                            default=None)
        parser.add_argument('--output')
        return parser


def write_to_file(parser, output):
    reader = csv.reader(fileinput.input(parser.args.file), delimiter=parser.args.delimiter)
    writer = csv.writer(output, delimiter=parser.args.delimiter)
    ts_key = parser.args.key
    for row in reader:
        ts = row[ts_key]
        if parser.args.timestamp_read is None:
            from_time = datetime.datetime.utcfromtimestamp(int(ts[:10]))
        else:
            from_time = datetime.datetime.strptime(ts, parser.args.timestamp_read)
        if parser.args.timestamp_write is None:
            to_time = from_time.isoformat()
        else:
            to_time = from_time.strftime(parser.args.timestamp_write)
        row[ts_key] = to_time
        writer.writerow(row)


def main(args):

    parser = Parser(args)
    try:
        if parser.args.output is None:
            write_to_file(parser, sys.stdout)
        else:
            with open(parser.args.output, 'w') as output:
                write_to_file(parser, output)
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    main(sys.argv[1:])