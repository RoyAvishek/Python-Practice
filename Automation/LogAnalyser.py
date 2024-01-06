# Log Analyzer: Write a script that reads a log file, 
# extracts relevant information (e.g., timestamps, error messages), 
# and generates a summary or report.


import re

def analyze_log(log_file):
    # Define regular expressions to extract timestamps and error messages
    timestamp_regex = r'\[(.*?)\]'
    error_regex = r'ERROR: (.*?)$'

    timestamps = []
    error_messages = []

    # Read the log file and extract relevant information
    with open(log_file, 'r') as file:
        for line in file:
            timestamp_match = re.search(timestamp_regex, line)
            if timestamp_match:
                timestamps.append(timestamp_match.group(1))

            error_match = re.search(error_regex, line)
            if error_match:
                error_messages.append(error_match.group(1))

    # Generate a summary report
    print("Log Analysis Report")
    print("-------------------")
    print("Total Log Entries:", len(timestamps))
    print("Timestamps:")
    for timestamp in timestamps:
        print(timestamp)
    print("Error Messages:")
    for error_message in error_messages:
        print(error_message)

# Specify the path or filename of the log file
log_file = "example.log"

# Call the log analyzer function
analyze_log(log_file)
