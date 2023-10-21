import os
import csv

# Define the root directory where class folders are located
root_folder = "/Users/jorgensandhaug/Documents/github_documents/automl/Data"  # Change this to the appropriate directory if needed

# Initialize an empty list to store rows for the CSV
csv_rows = []

# Loop through all directories and subdirectories
for root, dirs, files in os.walk(root_folder):
    for file in files:
        # Filter out only jpg files
        if file.endswith('.jpg'):
            # Full path to the image
            full_path = os.path.join(root, file)
            
            # Class label is the name of the folder
            class_label = os.path.basename(root)
            
            # Append to the list of rows for the CSV
            csv_rows.append([full_path, class_label])

# Write the rows to a CSV file
csv_file_path = "image_paths.csv"  # Change this to your desired output path
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header
    csv_writer.writerow(["image_path", "class_label"])
    
    # Write the rows
    csv_writer.writerows(csv_rows)

print(f"CSV file created at {csv_file_path}")

