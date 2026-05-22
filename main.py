import os
import questionary
files =  [x for x in os.listdir('.') if os.path.isfile(x)]
files.remove(os.path.basename(__file__))
folders = [f for f in os.listdir('.') if os.path.isdir(f)]

print(f"\n----------------- {len(files)} Files Found -----------------")

choice = input("Enter \033[1;32m1\033[0m: Automatically  \033[1;32m2\033[0m: Manually : ")
if choice == "1":
    for file in files:
        if "." not in file:
            continue
        folder_name = file.split('.')[-1]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        os.rename(file, f"{folder_name}/{file}")
elif choice == "2":
    extensions = {x.split('.')[-1] for x in files}
    running = True
    folder_and_type = dict()
    while running:
        if not extensions:
             break
        folder_name = input("\nWrite Folder Name (Enter To Cancel/Continue): ")

        if folder_name == "":
            break

        choices = questionary.checkbox(
            "Select file types:",
            choices=list(extensions)
            ).ask()
        for i in choices:
            folder_and_type[i] = folder_name
        for i in choices:
            extensions.remove(i)
    
    print("\n----------------- STRUCTURE -----------------")
    for file,folder in folder_and_type.items():
        print(f"{file} → ./{folder}")
    approvel = input("Do you want to continue (Y/n): ")
    if not approvel == "n":
        for file in files:
            if "." not in file:
                continue
            extension = file.split('.')[-1]
            if extension not in folder_and_type.keys():
                 continue
            folder_name = folder_and_type[extension]
            if not os.path.exists(folder_name):
                        os.mkdir(folder_name)
            os.rename(file, f"{folder_name}/{file}")
    else:
         print("Request Cancelled")


    