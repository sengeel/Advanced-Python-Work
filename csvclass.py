import csv

# Define some data
data = [
    {'Name': 'John', 'Age': 25},
    {'Name': 'Jane', 'Age': 30},
    {'Name': 'Bob', 'Age': 35}
]

# Write the data to a CSV file
with open('people.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Age'])
    writer.writeheader()
    writer.writerows(data)

# Read the data from the CSV file
with open('people.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)