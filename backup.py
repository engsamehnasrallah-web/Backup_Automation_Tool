import shutil
import datetime
import os

source_folder = input("Enter Folder Path: ")

if not os.path.exists(source_folder):
    print("Folder does not exist.")
    exit()

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_name = f"backup_{timestamp}"

shutil.make_archive(
    backup_name,
    'zip',
    source_folder
)

print(f"Backup Created: {backup_name}.zip")
input("Press Enter to exit...")