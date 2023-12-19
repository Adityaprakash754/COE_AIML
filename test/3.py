import csv

data = [
    ['Name','Age','City'],
    ['John Doe','25','New York'],
    ['Jame Smith','30','San Francisco'],
    ['Bob Johnson','32','Chicago']
]

csv_file_name = "example.csv"
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f"CSV file '{csv_file_name}' has been created.")