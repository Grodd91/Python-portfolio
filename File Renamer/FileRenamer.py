import os

folder_path = os.getcwd()  # Get the current folder path

file_counter = 1
for root, dirs, files in os.walk(folder_path):
    # Rename files
    for filename in files:
        new_filename = f"file{file_counter}"
        file_counter += 1
        os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
    
    # Convert folders into files
    for directory in dirs:
        new_filename = f"file{file_counter}"
        file_counter += 1
        os.rename(os.path.join(root, directory), os.path.join(root, new_filename))
