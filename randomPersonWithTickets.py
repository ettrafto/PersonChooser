import csv
import random

# Define the CSV file name
csv_file = 'names_and_tickets.csv'

# Create a list to store names and corresponding ticket counts
names_tickets_list = []

# Read names and ticket counts from the CSV file
try:
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'name' in row and 'numTickets' in row:
                name = row['name']
                num_tickets = int(row['numTickets'])
                names_tickets_list.append((name, num_tickets))
except FileNotFoundError:
    print(f"The file '{csv_file}' was not found.")
    exit(1)

# Check if the list is empty
if not names_tickets_list:
    print(f"The CSV file '{csv_file}' does not contain any data.")
    exit(1)

# Create a new list where each person's name is repeated based on their ticket count
all_names = [name for name, num_tickets in names_tickets_list for _ in range(num_tickets)]

# Check if there are any eligible people
if not all_names:
    print(f"No eligible participants found.")
    exit(1)

# Choose a random person from the new list
chosen_person = random.choice(all_names)

print(f"Randomly selected person: {chosen_person}")