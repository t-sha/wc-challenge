import argparse
import os

# Takes -c and returns number of bytes
#  -l that outputs the number of lines 
# -w that outputs the number of words in a file
# -m that outputs the number of characters in a file
# no options are provided, which is the equivalent to the -c, -l and -w options
# able to read from standard input if no filename is specified






#count bytes
def count_bytes(input_file):
    file_size = os.stat(input_file)
    return file_size.st_size

#count lines
def count_lines(input_file):
    num_lines = sum(1 for _ in open(input_file))
    return num_lines

#count words
def count_words(input_file):
    number_of_words = 0
    with open(input_file,'r') as file:
        data = file.read()
        lines = data.split()
        for word in lines:
            number_of_words += 1
    return number_of_words

#count characters
def count_characters(input_file):
    number_of_chars = 0
    with open(input_file,'r') as file:
        for line in file:
            number_of_chars += len(line) + 1
        return number_of_chars



# read arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='wc command line tool')
    parser.add_argument('filename')
    parser.add_argument('-c', action="store_true", dest='file_size', help="gets the byte count")
    parser.add_argument('-l', action="store_true", dest='line_count', help="gets the line count")
    parser.add_argument('-w', action="store_true", dest='word_count', help="gets the word count")
    parser.add_argument('-m', action="store_true", dest='char_count', help="gets the character count")
    args = parser.parse_args()

# action based on arguments
    if args.file_size:
        print(count_bytes(args.filename))

    if args.line_count:
        print(count_lines(args.filename))

    if args.word_count:
        print(count_words(args.filename))

    if args.char_count:
        print(count_characters(args.filename))

    #default action - do all