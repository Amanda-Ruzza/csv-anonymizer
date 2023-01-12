import csv
import hashlib
import logging

logger = logging.Logger(__name__)

HASH_SALT = "keij3ka2Hie2lilie1aiwab5oaQuooth"


def hash_field(field: str) -> str:
    salted_value = "{}{}".format(field, HASH_SALT)

    return str(hashlib.sha1(salted_value.encode("utf-8")).hexdigest())[:12]


def main():
    logger.info("main")
    # TODO set input file from cli argument
    # TODO no hardcoding file names
    with open('people-100.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # TODO set output file from cli argument
        # TODO no hardcoding file names
        with open('new-people-100.csv', 'w') as new_file:
            # TODO have an argument for if the csv has headers or not
            # TODO if the script is using header values which columns should we hash by header use DictReader
            # TODO if the script is not using header values which columns should we hash by column index use reader
            fieldnames = ['Index', 'First Name', 'Last Name', 'Email', 'Job Title']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter='\t')
            csv_writer.writeheader() # writes the header from the original CSV into the new one

            for line in csv_reader:
                line["Index"] = hash_field(line["Index"])
                csv_writer.writerow(line)


if __name__ == "__main__":
    main()