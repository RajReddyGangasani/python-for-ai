if not os.path.exists('data'):
    os.makedirs('data')
    print('Yes the file is created')
else:
    print("this file is alredy exists")


folders = ["images", "videos", "documents", "music"]          #here you are creating the subfolders inside the a main folder.

if not os.path.exists('project folders'):
    os.makedirs("project folders")

for folder in folders:                                       # in order to create each sub-folder indivudally insie the main folder we are using for loop.
    os.makedirs(f"project folders/{folders}", exist_ok=True) # here "exit_ok=True" is mandatory because it helps code to not to throw error if there a file already exists and helps code to skip that and move on.
    print("all folders are created")                         #here you creating the all subfolders in "project folders".

#to print the list of files in the current directory
import os

files= os.listdir()                    #os.listdir used to list all files in the local system.
print(files)

for f in files:                       #to print all file names in list one by one we are using for loop.
    print(f)
print(len(files))

#to delete the file in main directory 

import os   # Import the os module to work with system directories and files

# Loop through all items in the current directory
for folder in os.listdir():

    # Check if the item is a folder (not a file)
    if os.path.isdir(folder):

        # Get list of items inside the folder
        # If the folder is empty, os.listdir(folder) will return []
        # len([]) == 0 → folder is empty
        if len(os.listdir(folder)) == 0:

            # Remove the empty folder
            os.rmdir(folder)

            # Print confirmation for the user
            print("Deleted empty folder:", folder)
