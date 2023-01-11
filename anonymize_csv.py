import csv

with open('people-100.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #should I anonymize just the email field here?

    with open('new-people-100.csv', 'w') as new_file:
        fieldnames = ['Index', 'First Name', 'Last Name', 'Email', 'Job Title']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter='\t')
        csv_writer.writeheader() # writes the header from the original CSV into the new one

        for line in csv_reader:
            del line['First Name'] #deletes the 'First Name' field before writing to the new file
            csv_writer.writerow(line)