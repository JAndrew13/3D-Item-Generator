import json
import math
import random
import itertools

MULTIPLIER = .5
RARITY_VAlUES = []
WEIGHTS = {
    1: 40,
    2: 30,
    3: 25,
    4: 20,
    5: 15,
    6: 10,
    7: 6,
    8: 4,
    9: 3,
    10: 1
}

# Rarities = {'ID' : 'ID Value'}
rarities = {
    1: 'very common',
    2: 'common',
    3: 'uncommon',
    4: 'rare',
    5: 'super rare',
    6: 'ultra rare',
    7: 'exquisite',
    8: 'mythic',
    9: 'legendary',
    10: 'divine'
}

current_filename = ""
current_data = {}


# ------------------------------ MENU 1 (Create, Save, Load) -------------------------------- #

def menu_1():
    global current_filename, current_data
    print("\n Welcome to JB's Item Generator!\n")
    print("What would you like to do?")
    print("1. Create a new catalog.")
    print("2. Load Existing catalog.")
    answer = int(input("\n--->"))

    if answer == 1:
        current_filename = input('What would you like to name this file?')
        create_catalog(current_filename)

        current_data = load_catalog(current_filename)

    elif answer == 2:
        current_filename = input('Enter the name of the file you would like to load\n--->')
        current_data = load_catalog(current_filename)

    else:
        print("oops!")
        menu_1()


def create_catalog(filename):
    catalog = {}

    # Take info and build Catalog
    category_nums = int(input("\nHow many categories would you like to add?"))
    for category in range(category_nums):
        cat_name = input(f'What would you like to name category {category}?')
        catalog[cat_name] = []
        items_num = int(input(f'How many items are in the category {cat_name.upper()}?'))
        for i in range(items_num):
            catalog[cat_name].append(i)
    save_file(catalog, filename)


def save_file(data, filename):
    print('\npreparing to save updated data...')
    data = json.dumps(data)
    with open(f'data/{filename}.json', 'w') as file:
        file.write(data)
    print('File Saved!')


def load_catalog(filename):
    with open(f"data/{filename}.json", 'r') as data:
        current_catalog = json.load(data)

        print("File successfully loaded!")
        return current_catalog


# ------------------------------ MENU 2 : RARITY GENERATION (Auto/Manual) -------------------------------- #

def menu_2():
    global current_data
    # -------------------------MAIN MENU-----------------------------------------#
    print('\nWhat would you like to do next?')
    print('1. Automatically assign rarities to items')
    print('2. Modify item rarities')
    print('3. Continue to Generator')
    print('4. EXIT')

    path = int(input('\n Please select a number. \n --->'))

    # -------------------------OPTION 1 : SELECT SINGLE ITEM --------------------#
    if path == 1:
        current_data = auto_rarity()
        save_file(current_data, current_filename)

    # -------------------------OPTION 2 : Modify item Rarities -------------------------#
    elif path == 2:  # Combine items into sets.
        current_data = manual_rarity()
        save_file(current_data, current_filename)

    # -------------------------OPTION 3 : Continue to Generator --------------------#
    elif path == 3:

        for item in current_data:

            if len(current_data[item][0]) > 1:
                pass
            else:
                print('Rarities not yet assigned, returning to menu.')
                menu_2()

    # -------------------------OPTION 3 : EXIT THE GENERATOR---------------------#
    elif path == 4:  # exit the Item Generator
        print('goodbye!')

    # -------------------------  ERROR  --------------------------------#
    else:
        print("Sorry, please Enter a valid number.")
        menu_2()


def auto_rarity():
    new_data = {}

    # determine category name
    print("\nNew Item Rarities:")
    for category in current_data:
        name = category
        print(f"-={name.upper()}=-")
        items = []
        # build items data in category
        for item in current_data[category]:
            item_stats = []

            # determine item's data
            if type(item) == int:
                item_id = item
            else:
                item_id = item[0]
            item_rarity = rarities[(item_id + 1)]
            item_rarity_value = item_id

            # assign data to the item's list
            item_stats.append(item_id)
            item_stats.append(item_rarity)
            item_stats.append(item_rarity_value)

            print(f"Item #{item_id}: rarity - {item_rarity}")
            # assign the item's data to the categories list
            items.append(item_stats)

        # Compile all data into new catalog dictionary
        new_data[name] = items
    return new_data


def manual_rarity():
    # manual entry menu
    print('\n~Manual Rarity Selector~\n')
    new_catalog = {}
    print('Categories:')
    categories = []

    # Populate temporary categories list
    for category in current_data:
        categories.append(category)

    # Editing Item Rarities
    while len(categories) > 0:
        print("")

        # Take input from user
        n = 0
        if len(categories) != n:
            for category in categories:
                print(f'{n}. {category}')
                n += 1
            answer = int(input('\nPlease enter the category number to edit\n ---> '))
            choice = categories[answer]

            # Editing Single Category (loop)
            editing_category = True
            while editing_category:
                # determine chosen category
                print(f'\ncategory : {choice}')

                # Build items list
                items = []

                # display rarity reference
                print("\n-= RARITIES REFERENCE =-")
                for item in rarities:
                    print(f"{item}. {rarities[item]}")

                for item in current_data[choice]:
                    item_stats = []

                    # determine item rarity and item_rarity_id
                    item_rarity_id = int(input(f"\nenter a rarity for (CATEGORY: {choice.upper()}, ITEM #{item})\n--->"))
                    item_rarity = rarities[item_rarity_id]

                    # Append new item stats to Item list
                    item_stats.append(item)
                    item_stats.append(item_rarity)
                    item_stats.append(item_rarity_id)

                    # Append completed item stats to Items List
                    items.append(item_stats)
                    new_catalog[choice] = items
                    # Print results to user

                n = 0
                print(f'\nNew stats for CATEGORY: {choice.upper()}')
                for i in items:
                    print(f'Item #{n} - Rarity: {i[1].upper()}')
                    n += 1

                categories.pop(answer)
                editing_category = False

    print('\nAll Categories updated!')
    for category in new_catalog:
        print(f"-={category.upper()}=-")
        for item in new_catalog[category]:
            print(f"Item #{item[0]} - {item[1]}")

    response = int(input("Enter '1' to save data, or '2' to re-do editing ."))
    if response == 1:
        print(f"New Catalog : {new_catalog}")
        return new_catalog
    elif response == 2:
        manual_rarity()


# ---------------------------------GENERATOR TOOLS-----------------------------------#

def get_max(categories_to_use, gen_type):

    total = []
    for category in categories_to_use:
        amount = len(current_data[category])
        total.append(amount)
    if gen_type == 'single':
        max_quantity = sum(total)
    elif gen_type == 'combo':
        max_quantity = math.prod(total)

    return max_quantity


def quality_list(rarity_value):
    values = [100]
    for i in range(len(rarities)):
        n = values[i]
        n -= n * MULTIPLIER
        num = round(n, 2)
        values.append(num)
    values.pop(0)
    return values[rarity_value]


def item_quantity(categories_to_use):
    items = []
    for category in categories_to_use:
        category_items = []
        for item in current_data[category]:
            category_items.append(item)
        items.append(len(category_items))


# --------- MENU 3 : GENERATION DATA (singles/sets, duplicates, categories, quantity ----------#

def menu_3():
    print("\n-=ITEM GENERATOR MENU=-")
    print("How would you like to generate items")
    print("1. Generate random single items")
    print("2. Generate random SETS of items")
    answer = int(input("\nPlease enter selected number.\n--->"))

    categories_to_use = []
    all_categories = []

    for item in current_data:
        all_categories.append(item)

    # Take user input for generation data
    done = False
    print("")
    while not done:
        n = 0
        for category in all_categories:
            n += 1
            print(f'{n}. {category}')

        # What categories should be used?
        category_add = int(input("\nPlease select a category number to add to generator.\nEnter '0' when DONE.\n--->"))
        if category_add == 0:
            done = True
        elif len(all_categories) == 0:
            print(f"\nSelected Categories : {categories_to_use}\n")
            done = True
        else:
            categories_to_use.append(all_categories[(category_add - 1)])
            all_categories.pop(category_add - 1)
            print(f"\nSelected Categories : {categories_to_use}\n")

    # Will you allow duplicate items?
    dupes = int(input("\nWill you allow duplicate items to be created?\nEnter '1' for YES, or '2' for NO\n--->"))

    if dupes == 1 and answer == 1:
        # Single Gen + allow dupes
        duplicates = True
        generate_singles(categories_to_use, duplicates)

    elif dupes == 2 and answer == 1:
        # Single Gen + no dupes
        duplicates = False
        generate_singles(categories_to_use, duplicates)

    elif dupes == 1 and answer == 2:
        # Combo Gen + allow dupes
        duplicates = True
        generate_combos(categories_to_use, duplicates)

    elif dupes == 2 and answer == 2:
        # Combo Gen + no Dupes
        duplicates = False
        generate_combos(categories_to_use, duplicates)

    else:
        print('invalid input.')
        menu_3()


def generate_singles(categories_to_use, duplicates):
    if duplicates:
        make_amount = int(input("Enter the amount of items you would like to generate:\n--->"))

    elif not duplicates:
        max_amount = get_max(categories_to_use, 'single')
        make_amount = int(input(f"Enter the amount of items you would like to generate:"
                                f"\n~MAX amount is {max_amount}~\n--->"))

        if make_amount > max_amount:
            generate_singles(categories_to_use, duplicates)

    items = []
    rarity = []
    generated_items = []
    n = 0
    print("")

    # define items to choose from
    for category in categories_to_use:
        for item in current_data[category]:
            item.append(category)
            items.append(item)

    # apply random chance to each item based on rarity code
    for item in items:
        value = 100 * (0.5 ** (item[2] + 1))
        rarity.append(value)

    while make_amount > 0:
        n += 1

        # Generate random item from list of available Items
        if not duplicates:
            obj = random.choices(items, rarity, k=1)

            # determine index of selected item
            index_val = items.index(obj[0])

            # remove selected item and rarity val from available choices
            rarity.pop(index_val)
            items.pop(index_val)

            # add selected item to list of generated items
            generated_items.append(obj[0])

        # If duplicates don't matter, then pick random item
        elif duplicates:
            obj = random.choices(items, rarity, k=1)
            generated_items.append(obj[0])

        # Then Display result and reduce 'to_make' count
        make_amount -= 1
        print(f"{n}. {obj[0][3].upper()}: , ID:{obj[0][0]}, Rarity: {obj[0][1].upper()} ")

    print(f"\n{n} new items have been created!")


def generate_combos(categories_to_use, duplicates):
    # ------------- TAKE USER INPUT ---------------- #

    # If duplicates are allowed
    if duplicates:
        to_make = int(input("Enter the amount of item combos you would like to generate:\n--->"))

    # if duplicates are NOT allowed
    elif not duplicates:
        max_amount = get_max(categories_to_use, 'combo')
        to_make = int(
            input(f"Enter the amount of item combos you would like to generate:\n~MAX amount is {max_amount}~\n--->"))

    # ~~~~~~~~~~~~~~~GENERATE NEW TEMPORARY SELECTION CATALOG~~~~~~~~~~~~~~#
    categories = {}

    for category in categories_to_use:
        values = []
        for item in current_data[category]:
            value = 100 * (0.5 ** (item[2] + 1))
            values.append(value)

        items = [current_data[category], values]

        categories[category] = items
    for category in categories:
        for item in categories[category][0]:
            item.append(category)

    # ~~~~~~~~~~~~~GENERATE ITEMS~~~~~~~~~~~~#

    gen_dict = {}
    n = 0

    if duplicates:
        # generate random combo
        while to_make > 0:
            new_combo = {}
            for category in categories_to_use:
                selection_rarities = []
                for item in categories[category][0]:
                    selection_rarities.append(item[2])
                selection_weights = []
                for item in selection_rarities:
                    selection_weights.append(WEIGHTS[item])

                obj = (random.choices(categories[category][0], selection_weights, k=1))
                new_combo[category] = (obj[0][0])

            gen_dict[n] = new_combo
            n += 1
            to_make -= 1
        print(f'\n-= Successfully created {len(gen_dict)} unique new items! =-')
        print(gen_dict)
    elif not duplicates:

        id = 0

        # Generate Master List of categories + items : item id's as "iter_list"
        # ex. ITER LIST : [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
        iter_list = []
        for category in categories_to_use:
            category_items = []
            for item in current_data[category]:
                category_items.append(item[0])
            iter_list.append(category_items)

        # Determine all possible combinations into list "results"
        results = list(itertools.product(*iter_list))

        # Create Dictionary to store combinations
        TEMP_COMBINATIONS = {}

        # Fill Combo Dictionary { "id": { "Category" : "item" } }
        for combo in results:
            creation = {}
            n = 0
            for category in categories:
                creation[category] = combo[n]
                n += 1
            TEMP_COMBINATIONS[id] = creation
            id += 1

        # Save All Possible combos to file
        print(f"\ngenerating all possible combinations as -={current_filename}_MaxCombos.json=-")
        filename = f"{current_filename}_MaxCombos"
        save_file(TEMP_COMBINATIONS, filename)

        # populate selection id's
        id_list = []

        for num in range(0, len(TEMP_COMBINATIONS)):
            id_list.append(num)

        id = 0
        while to_make > 0:
            # chose random index number from ALL
            selection = int(random.choice(id_list))

            # add the item info from TEMP_COMBINATIONS to dictionary
            gen_dict[id] = TEMP_COMBINATIONS.get(selection)

            # find the index of selection in id_list
            selection_index = id_list.index(selection)

            # remove the id number from list
            id_list.pop(selection_index)

            # increment id counter
            id += 1

            # decrement to_make count
            to_make -= 1

        print(len(gen_dict))
    print(f"Saving generated combos to -={current_filename}_GeneratedCombos.json=-")
    # Save new data to separate file
    filename = f"{current_filename}_GeneratedCombos"
    save_file(gen_dict, filename)



menu_1()
menu_2()
menu_3()

