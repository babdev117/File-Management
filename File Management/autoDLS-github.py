import os
import shutil

img = (
    ".jpeg", ".png", ".png", ".gif", ".svg", ".ai"
    )

pdf = (
    ".pdf", ".pptx", ".doc", ".docx", ".xls", ".xlsx", ".ppt"
    )

# exe = (
#     ".exe"
#     )

source_dir = r"FILE PATH OF DIRECTORY TO BE MOVED"
dest_dir_images = r"YOUR FILE PATH OF DIRECTORY FOR IMAGES TO BE MOVED TO"
dest_dir_pdf = r"YOUR FILE PATH OF DIRECTORY FOR PDF's AND MISC TO BE MOVED TO"

# These functions are checking for the extension of the file. Postion 0 is the file name. Postion 1 is the file extension i.e. ".jpeg" or ".pdf"
def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

def is_image(file):
    return os.path.splitext(file)[1] in img

## Use this to move executable files, i use it for downloaded app exe's when i have reinstalled windows. 
# def is_exe(file):
#     return os.path.splitext(file)[1] in exe

# Directing the script to get into the source directory that contains all the files to be moved.
os.chdir(source_dir)

# This loop iterates through all the files in the source directory, 
# decides if any exentions are present that the script wants to move, then moves the files to the destination directory
for file in os.listdir(source_dir):
    if is_pdf(file):
        shutil.move(file, dest_dir_pdf)
    elif is_image(file):
        shutil.move(file, dest_dir_images)

print("Your files have been moved to the destination folders.")

