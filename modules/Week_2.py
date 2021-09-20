# this is an empty file to make python understand that this is a module

import argparse
import csv


def print_file_content(file):
    with open(file) as file_object:
        content = file_object.read()
    print(content)

    
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for element in lst:
            file_object.write('%s\n' % element)

            


            
def read_csv(input_file):
    lst = []
    with open(input_file, 'r') as file_object:
        lst = file_object.read().splitlines()
    return lst

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that can take an input and an output file and write the content of the input file into a list, the console or to the output file.')
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('--file', help='Name of the output file')
    args = parser.parse_args()

    if args.file is None:
        print_file_content(args.input_file)
    else:
        lst = read_file(args.input_file)
        write_list_to_file(args.file, lst)
        print(lst)