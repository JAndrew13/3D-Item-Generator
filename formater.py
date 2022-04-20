import json
import random

filename = "potheads"

OBJ_DIRECTORY_1 = "C:\\Users\\Leaf\\Desktop\\ItemGenerator_1.1\\objects\\"
TRANSLATED_COMBOS = {}
PAINT_COLORS = ["_blue", "_red", "_green", "_yellow", "_orange", "_purple", "_white"]
PAINT_RARITY = ["_very_common","_common","_uncommon","_rare","_super_rare","_ultra_rare","_exquisite"]

def load_catalog(filename):
    with open(f"data/{filename}_GeneratedCombos.json", 'r') as data:
        current_catalog = json.load(data)

        print("File successfully loaded!")
        return current_catalog

def get_paint(paint_code):
    paint_nametype = PAINT_RARITY[paint_code]
    return paint_nametype

def get_color(pot_number):
    paint_color = PAINT_COLORS[pot_number]
    return paint_color

def name_translator(set):
    global TRANSLATED_COMBOS
    # get items from set and create the item codes

    paint_code = set["paint"]
    set.pop("paint")
    paint_nametype = get_paint(paint_code)
    paint_color = ""
    if paint_code == 1:
        paint_color = get_color(set["pot"])

    set_list = []

    # Remove ears from pot 6 and 7
    if set["pot"] >= 4:
        set.pop("ears")

    for category in set:
        item_category = category
        item_number = set[category]

        # for plants
        if item_category == "plant":
            item_code = f"${item_category}_{item_number}"
            set_list.append(item_code)

        # for nose and mouth
        elif item_category == "nose" or item_category == "mouth":
            item_code = f"${item_category}_{item_number}{paint_nametype}{paint_color}"
            set_list.append(item_code)

        else:
            item_code = f"${item_category}_{item_number}{paint_nametype}"
            set_list.append(item_code)


    print(set_list)
    return set_list


# filename = input(f"Enter the name of the project file you would like to load.\n--->")
current_catalog = (load_catalog(filename))

for set_number in current_catalog:
    TRANSLATED_COMBOS[int(set_number)] = name_translator(current_catalog[set_number])



# Pull script Template and create combo files
def populate_script_templates():
    with open("data/script_template.txt", "r") as template:
        lines = template.readlines()
        for set_number in TRANSLATED_COMBOS:
            f = open(f"scripts/Combo_{set_number}_Script.txt", "w")
            for line in lines:
                f.write(line)
            f.close()

def customize_script_templates():

    # Open each set's blueprint script
    for set_number in TRANSLATED_COMBOS:

        FILENAME=f"scripts/Combo_{set_number}_Script.txt"
        old_combo_script = open(FILENAME)


        # Pull set data from TRANSLATED_COMBOS list --> format data into a usable string
        combo_data_string = ""
        for set_item in TRANSLATED_COMBOS[set_number]:
            combo_data_string += f"{set_item}, "
        fixed_string = combo_data_string[:-2]

        # Create new line replacement data
        new_item_string = f"MySelection = #({fixed_string})"
        replace_line(FILENAME, 0, new_item_string)

        replace_line(FILENAME, 27, f'combonum ="{set_number}"')

        new_item_dir = 'dir='f'"{OBJ_DIRECTORY_1}"'
        replace_line(FILENAME, 0, f"{new_item_string}\n")

        replace_line(FILENAME, 28, f"{new_item_dir}\n")
        old_combo_script.close()

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()




populate_script_templates()
customize_script_templates()






