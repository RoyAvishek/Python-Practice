# File Backup Utility: Write a program that scans a directory and its subdirectories, 
# identifies files that have been modified recently, and creates a backup of those files.

import os
import shutil
import datetime

def backup_recently_modified_files(source_dir, backup_dir, days_threshold):
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Calculate the threshold date by subtracting the specified days
    threshold_date = current_datetime - datetime.timedelta(days=days_threshold)

    # Walk through the source directory and its subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Check if the file has been modified recently
            if file_modified_time > threshold_date:
                # Create the corresponding directory structure in the backup directory
                relative_path = os.path.relpath(file_path, source_dir)
                backup_file_path = os.path.join(backup_dir, relative_path)

                # Create the backup directory if it doesn't exist
                os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)

                # Copy the file to the backup directory
                shutil.copy2(file_path, backup_file_path)

                print(f"Backed up file: {file_path}")

# Specify the source directory to scan for recently modified files
source_directory = "/path/to/source/directory"

# Specify the backup directory to store the backup files
backup_directory = "/path/to/backup/directory"

# Specify the number of days to consider for recently modified files
days_threshold = 7

# Call the backup_recently_modified_files function
backup_recently_modified_files(source_directory, backup_directory, days_threshold)
