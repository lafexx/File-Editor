import os

print("This is a script that renames files in a directory.")
print("To get started type in the location of the folder that contains the files you want to modify")
print("made by lafe of course ;)")

# save what the user types in as a variable
folder = input("Folder location: ")

_continue = False

# main rename func


def rename_operation(folder):
    # ask what the user wants to rename the files to
    new_name = input("What do you want to rename the files to?")

    # create an int to keep track of how many of the same file name there are
    count = 0

    # for each file in the folder
    for filename in os.listdir(folder):
        # if a file with the new name already exists
        if os.path.exists(os.path.join(folder, new_name)):
            # add 1 to count
            count += 1
            # if a file with the new name + count already exists
            if os.path.exists(os.path.join(folder, new_name + str(count))):
                # rename the file to the new name + count + 1
                os.rename(os.path.join(folder, filename), os.path.join(
                    folder, new_name + str(count + 1)))
            else:
                # rename the file to the new name + count
                os.rename(os.path.join(folder, filename),
                          os.path.join(folder, new_name + str(count)))
        else:
            # rename the file to the new name
            os.rename(os.path.join(folder, filename),
                      os.path.join(folder, new_name))


# main edit func
            
def edit_operation(folder):
    # do you want to remove or add to the file name
    op_ = input("Do you want to (R)emove or (A)dd to the file name?")
    # if the user types in R
    if op_ == "R":
        # what do you want to remove from the name
        remove = input("What do you want to remove from the name?")
        # for each file in the folder
        for filename in os.listdir(folder):
            # rename the file to the new name
            os.rename(os.path.join(folder, filename),
                      os.path.join(folder, filename.replace(remove, "")))
    elif op_ == "A":
        # what do you want to add to the name
        add = input("What do you want to add to the name?")
        # for each file in the folder
        for filename in os.listdir(folder):
            # rename the file to the new name
            os.rename(os.path.join(folder, filename),
                      os.path.join(folder, filename + add))


def rename_files(folder):
    # what operation do you want to perform?
    op = input("What operation do you want to use? (R)ename or (E)dit?")
    # if the user types in R
    if op == "R":
        rename_operation(folder)
    elif op == "E":
        edit_operation(folder)


# check to see if the user typed in a valid location
if os.path.isdir(folder):
    print("Folder found")
    # check to see how many files are in the folder
    numFiles = len(os.listdir(folder))
    print("There are " + str(numFiles) + " files in this folder")
    _continue = True
else:
    print("Folder not found")

if _continue == True:
    # ask the user if they want to rename the files
    rename = input("Do you want to rename the files? (y/n) ")
    if rename == "y":
        rename_files(folder)
    else:
        print("Ok, no files were renamed")
