#!/usr/bin/python3

import argparse

def set_from_file(f):
    file_set = set()
    for line in f:
        file_set.add(line.rstrip('\n'))
    return file_set

def get_result(args):
    return get_result_mapped_args(args.file1, args.file2, args.operation)

def get_result_mapped_args(f1, f2, op):
    file1_set = set_from_file(f1)
    file2_set = set_from_file(f2)

    result_set = set()
    if op in ['i', 'intersect']:
        result_set = file1_set & file2_set
    elif op in ['u', 'union']:
        result_set = file1_set | file2_set
    elif op in ['d', 'difference']:
        result_set = file1_set - file2_set
    elif op in ['rd', 'rdifference']:
        result_set = file2_set - file1_set

    return result_set

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', help='The operation to run: i(ntersect), u(nion)',
            choices=['i', 'intersect', 'u', 'union', 'd', 'difference', 'rd', 'rdifference'])
    parser.add_argument('file1', type=argparse.FileType('r'), help='The first file')
    parser.add_argument('file2', type=argparse.FileType('r'), help='The second file')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    result = get_result(args)
    for r in result:
        print(r)
