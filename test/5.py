import csv

column_to_read = 'Name'
with open('example.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    column_index = header.index(column_to_read)

    for row in csv_reader:
        print(row[column_index])