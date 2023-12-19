import csv

data = [
    ['Customer Name','Age','Phone Number','Total Purchase Amount'],
    ['John Doe','25','1234567890','1000'],
    ['Jame Smith','30','124567890','2000'],
    ['Bob Johnson','32','1234567890','3300']
]

csv_file_name = "shop.csv"
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f"CSV file '{csv_file_name}' has been created.")