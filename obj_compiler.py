# import subprocess

# # Open 3DS Max Starting file
# subprocess.Popen(r'explorer /open,"C:\Users\Leaf\Desktop\ItemGenerator_1.1\files\PotHead_Compile.max"')

# open Starting Script
# subprocess.Popen(r'explorer /open,"C:\Users\Leaf\Desktop\ItemGenerator_1.1\scripts\test_script.ms"')

import os.path
import random

# CHANGE THESE VARIABLES FOR INDIVIDUAL USE
OBJ_IN_FILEPATH = "C:\\Users\\Leaf\\Desktop\\ItemGenerator_1.1\\files\\OBJ_Compile.max"
OBJ_OUT_FILEPATH = "C:\\Users\\Leaf\\Desktop\\ItemGenerator_1.1\\objects"
SCRIPTS_FILEPATH = "C:\\Users\\Leaf\\Desktop\\ItemGenerator_1.1\\scripts"
SCRIPT_MANAGER_ALL_FILEPATH = "scripts/script_manager_all.txt"
SCRIPT_MANAGER_SOME_FILEPATH = "scripts/script_manager_some.txt"

TOTAL_OBJ_SCRIPTS = {}


def get_scripts():  #---> Return dictionary of line_num : filepaths
    path, dirs, files = next(os.walk(SCRIPTS_FILEPATH))
    script_paths = []

    script_id = 0
    for file in files:
        script_paths.append(f'fileIn "{file}"')
    return script_paths


def create_script_manager_all():
    script_paths = get_scripts()
    with open(SCRIPT_MANAGER_ALL_FILEPATH, 'a') as f:
        f.write('\n'.join(script_paths))

def create_script_manager_some():
    script_paths = get_scripts()
    new_script_paths = []

    count = int(input("How many combos would you like to generate?\n--->"))
    while count != 0:
        selection_index = random.randint(0, len(script_paths))
        new_script_paths.append(script_paths[selection_index])
        script_paths.pop(selection_index)
        count -=1
    with open(SCRIPT_MANAGER_SOME_FILEPATH, 'a') as f:
        f.write('\n'.join(new_script_paths))

def obj_compiler_menu():
    answer = int(input("-= OBJECT COMPILER =- \n1. Compile ALL possible scripts.\n2. Compile SOME scripts.\n--->"))
    if answer == 1:
        create_script_manager_all()
        print(f"Script Manager compiled and ready!\n file location @ {SCRIPT_MANAGER_ALL_FILEPATH} ")
    elif answer ==2:
        create_script_manager_some()
        print(f"Script Manager compiled and ready!\n file location @ {SCRIPT_MANAGER_SOME_FILEPATH} ")
    else:
        print("invalid input, please retry!")
        obj_compiler_menu()

obj_compiler_menu()