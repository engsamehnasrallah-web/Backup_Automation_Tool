import shutil
import datetime
import os

backup_folder = "Backups"
source_folder = input("Enter Folder Path: ")

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

if not os.path.exists(source_folder):
    print("Folder does not exist.")
    exit()

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_name = os.path.join(
    backup_folder,
    f"backup_{timestamp}"
)

shutil.make_archive(
    backup_name,
    'zip',
    source_folder
)

with open("backup.log", "a") as log:
    log.write(
        f"[{timestamp}] Backup Created Successfully\n"
    )

print(f"Backup Saved To: {backup_name}.zip")
print(os.path.abspath(f"{backup_name}.zip"))
input("Press Enter to exit...")