import datetime
import os

# Static user info
user_id = 201
medication_name = "CTI-1601"

# Get the current date and time
current_datetime = datetime.datetime.now()
current_date = current_datetime.date()

# Format the current date and time
formatted_datetime = current_datetime.strftime("%B %d, %Y at %I:%M %p")

# Define the starting date of the injection cycle
start_date = datetime.date(2025, 4, 1)

# Calculate the number of days since the start date
days_elapsed = (current_date - start_date).days
day_number = days_elapsed + 1  # Include the start date as Day 1

# Determine the injection site from an 8-day rotation
injection_sites = [
    "Upper left-side abdomen",
    "Lower left-side abdomen",
    "Upper left thigh",
    "Lower left thigh",
    "Lower right thigh",
    "Upper right thigh",
    "Lower right-side abdomen",
    "Upper right-side abdomen"
]
rotation_index = days_elapsed % 8
injection_site = injection_sites[rotation_index]

# Create output text
output_text = (
    f"User ID: {user_id}\n"
    f"Medication: {medication_name}\n"
    f"Today's date and time: {formatted_datetime}\n"
    f"Day Number: {day_number}\n"
    f"Injection Site Location: {injection_site}\n"
)

# Print to console
print(output_text)

# Define file path
log_directory = r"C:\Users\garre\Documents"
log_file_path = os.path.join(log_directory, "injection_log.txt")

# Write to file
with open(log_file_path, "a") as file:
    file.write(output_text + "\n")  # Add extra newline for readability

