import csv

with open('newnames.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    # next(csv_reader)
    for line in csv_reader:
        print(line)
    # with open('newnames.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
    #     for lin in csv_reader:
    #         csv_writer.writerow(lin)
