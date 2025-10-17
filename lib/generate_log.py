from datetime import datetime
import os
import csv

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list
    if isinstance(data,list):
        filename=f"log_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(filename,"w",newline="") as file:
            writer=csv.writer(file)

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename