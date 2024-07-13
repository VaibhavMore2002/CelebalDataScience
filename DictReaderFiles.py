import csv
with open('namedetails.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('newnames.csv', 'w') as file_name:
        fieldnames = ['First_Name', 'Last_Name']
        csv_writer = csv.DictWriter(
            file_name, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['Email']
            csv_writer.writerow(line)
