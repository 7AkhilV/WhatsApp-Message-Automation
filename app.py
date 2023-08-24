import pywhatkit
import datetime

# Get user input for messages and phone numbers
messages_input = input("Enter messages (comma-separated): ")
phone_numbers_input = input("Enter phone numbers (comma-separated): ")

# Split user input into lists
messages = messages_input.split(',')
phone_numbers = phone_numbers_input.split(',')

# Get the current time
current_time = datetime.datetime.now()
scheduled_time = current_time + datetime.timedelta(minutes=2)  # Adding 2 minutes

# Loop through phone numbers and send messages
for phone_number in phone_numbers:
    for message in messages:
        pywhatkit.sendwhatmsg(phone_number, message, scheduled_time.hour, scheduled_time.minute) 

print("Messages sent!")