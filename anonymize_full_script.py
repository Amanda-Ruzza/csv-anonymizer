
import csv
import hashlib
import logging
import sys, getopt

logger = logging.Logger(__name__)

HASH_SALT = "keij3ka2Hie2lilie1aiwab5oaQuooth"

# This the function where we want to entry the script
def main(argv):
    inputfile = ''
    outputfile = ''
    columnnames = []
    try:
       opts, args = getopt.getopt(argv[1:],"hi:o:c:",["ifile=","ofile=", "column="])
    except getopt.GetoptError:
       print (f"{argv[0]} -i <inputfile> -o <outputfile> -c <columnname>")
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
           print (f"{argv[0]} -i <inputfile> -o <outputfile> -c <columnname>")
           sys.exit()
       elif opt in ("-i", "--ifile"):
           inputfile = arg
       elif opt in ("-o", "--ofile"):
           outputfile = arg
       elif opt in ("-c", "--column"):
           columnnames = arg.split(',')

    logger.info('Input file is: ', inputfile)
    parse_file(inputfile, outputfile, columnnames)
    logger.info('Output file is: ', outputfile)

def hash_field(field: str) -> str:
    salted_value = "{}{}".format(field, HASH_SALT)
    return str(hashlib.sha1(salted_value.encode("utf-8")).hexdigest())[:12]


def parse_file(input_file_name, output_file_name, columns_to_hash):
    with open(input_file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(output_file_name, 'w') as new_file:
            # TODO have an argument for if the csv has headers or not
            # TODO if the script is using header values which columns should we hash by header use DictReader
            # TODO if the script is not using header values which columns should we hash by column index use reader
            fieldnames = next(csv_reader)
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter='\t')
            csv_writer.writeheader() # writes the header from the original CSV into the new one

            for line in csv_reader:
                for column in columns_to_hash:
                    line[column] = hash_field(line[column])
                    
                csv_writer.writerow(line)


if __name__ == "__main__":
    main(sys.argv)