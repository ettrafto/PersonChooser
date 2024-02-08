import csv
import random

# Define the CSV file name
csv_file = 'names.csv'

# Create an empty list to store the names
names_list = []

# Read the names from the CSV file
try:
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                names_list.extend(row)
except FileNotFoundError:
    print(f"The file '{csv_file}' was not found.")
    exit(1)

# Check if the list is empty
if not names_list:
    print(f"The CSV file '{csv_file}' does not contain any names.")
    exit(1)

# Choose a random person from the list
random_person = random.choice(names_list)

print(f"Randomly selected person: {random_person}")