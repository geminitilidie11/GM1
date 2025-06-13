# Import library
import datetime

# Set current time varible
today = datetime.date.today ()

# Print today's date
formatted = today.strftime("%B %d, %Y")
print("Today's date:", formatted)

# Set static time varible
day_one = datetime.date (2025, 4, 1)

# Calculate current length of time
current_day = today - day_one

# Convert length of time in days
day_num = current_day.days

# Present findings 
print ("Total number of days:", day_num + 1)

# Calculate the cycle using a modulator
isl = day_num % 8

# Show calculations 
print('Day of rotation:', isl + 1)

# Loop of varible associations to complete formula using a string value
 
if isl == 0:
	isl = "Upper left-side abdomen"
elif isl == 1:
	isl = "Lower left-side abdomen"
elif isl == 2:
	isl = "Upper left thigh"
elif isl == 3:
	isl = "Lower left thigh"
elif isl == 4:
	isl = "Lower right thigh"
elif isl == 5:
	isl = "Upper right thigh"
elif isl == 6:
	isl = "Lower right-side abdomen"
elif isl == 7:
	isl = "Upper right-side abdomen"

# Final function
print("Injection Site Location:", isl)
