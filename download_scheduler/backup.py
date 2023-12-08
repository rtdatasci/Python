import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/rajee/Picutres/Screenshots"
destination_dir = "C:Users/rajee/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("16:24").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# runs as long as the python file is running
while True:
    schedule.run_pending() # looks for schedule task till the appointed time
    time.sleep(60) # add sleep so that it won't look for schedule every second
