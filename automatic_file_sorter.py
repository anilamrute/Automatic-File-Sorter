import os
import shutil

# Define the base path
path =r"C:/Users/Admin/Pictures/"

# Initialize folder mapping dynamically
folder_mapping = {}
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[-1].lower()
        if file_ext not in folder_mapping:
            folder_name = f"{file_ext.lstrip('.')} files"
            folder_mapping[file_ext] = folder_name

# Create folders if they don't exist
for folder in set(folder_mapping.values()):
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Sort files into their respective folders
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[-1].lower()
        if file_ext in folder_mapping:
            dest_folder = os.path.join(path, folder_mapping[file_ext])
            shutil.move(file_path, os.path.join(dest_folder, file))
