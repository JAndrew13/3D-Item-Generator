# JB's 3DS Max Item Generator
## Summary
This application is meant to be used as logistical support tool when creating a large collection of varied 3D objects. It was intially created for a digital art project I was working on, but was also written as a multi-tool for other projects in the future.  

# For final results of the project, please take a look at https://www.polypot.org/
*This website was hosted on Squarespace, but all other frontend elements (graphics, interactive 3D, blog posts, etc.) were created by me.


## How it works

It starts by building a JSON database file of objects types, categories, and amounts, and then randomly assembling them into new "combo" objects based on user preferences. 

Once the database has been created successfully, then walks through each generated object and creates an unique assemby script file,  as well as a batch script to be used in 3DS max (3D modeling software). When activated in the software, these scripts will grab all of the relevant 3d modeled parts, join them together, and export them as .OBJ files as well as .GLTF files. 

** The GLTF files specifically are extremely useful, because they come packed with with full texture/shader support, and are fully interactive and viewable in a web browser. 

## Disclaimer
This program was one of the first pieces of software i've written thus it is extremely fragile. Please be patient when using it, and make sure to respond to each prompt carefully, as the application doesnt have many "fail safes" and can crash easily!

## Requirements
 - Python 3.1
 - 3DS Max 2021 (or compatable version)

## Step by Step Instructions
** For simplicities sake, I will explain this using a Mr. Potato Head example with 7 categories of parts, and 3 types of each category. (ex. eyes, ears, nose, mouth, body, arms, and legs) 

This collection would theoretically have 21 unique 3D modeled parts. 


### Creating a new catalog
 - this option creates a new .json file with the base details of your 3d models, categories, and amounts

	1. Name the catalog
	- choose something simple that descibes the overall project. (ex. "potatoheads")
	2. Determine the total amount of categories.
	- When entering the categories amount, use an integer. (ex. "7")
	3. Name each category
	- starting a count from 0, type the name of each category, then enter the amount of parts in that category. 
(ex. "ears", then "3")

	4. Load Existing Catalog
 - Optionally, this loads an existing .json catalog previously created by the application

### Using the Catalog
	1. Automatically assign rarities to all items
	- this is typically the best way to go. it auto generates a rarity modifier, and applies it to each part per category. As the algorith cycles through the items in each category, the associated rarity value increases.
	(ex. ear_1 = .5, ear_2 = .25, ear_3 = .125, etc.)

	*** If creating a catalog for the first time, you should always auto assign rarites to the catalog before continuing to the generator. ***

	2. Modify item rarities
	- This option is used when you want to manually go through each part/category and add custom rarity values.

### The Generator

	1. Generate Random single items
	*** this feature is still in development ***
	- using this option, the generator will apply rarities to each part, and when producing the final selection, will return only individual parts as selections. This is good if you are producing a list of parts that wont be combined together.
	- you will be asked what categories to include in the selection set, aswell as how many random items to choose from the list. 

	2. Generate random combinations of items
	- This option allows you to create 

	- when using this feature, you will first decide what categories to include in the generator. Once complete, You will need to decide if you want to allow duplicates to be chosen. Allowing duplicates will give the most "True" results, because it accounts for item rarity when fetching each combinaton. 

	Alternatively, you can choose not to allow duplicates. In this case, the app will only produce combinations of items that havent yet been presented. To generate all possible item combinations, select this option along with the "max amount" value displayed in the console. 

	- Once you have determined all the generation parameters, go ahead and generate your combinations. If successful, you should now have a .JSON file in the apps "data" folder called "YourCollectionName"_GeneratedCombos.JSON"

This JSON file creates an ID number for each combination, along with the associated part number for each category.

*** The functions listed below are still very much built "project specific" and will need tweaking to allow for multi-funtionality use***

### Generating 3DS Max scripts from JSON Database
Once youve created your Gen. Combos database, youll need to run the formater.py file to generate a assembly script for each of your object combinations. This portion of the application goes cycles through each item in the database, and creates a .txt file script from the "script_template.txt" file in the data folder. 

### Using the Object Compiler

Once all the scripts have been created, the next step is to open the ObjectCompiler.py file. When initiated, you will need to modify lines 13 - 17. These variables hold the file directories for a few different things. 
 - OBJ_IN_FILEPATH (the .max file containing all 3d models)
 - OBJ_OUT_FILEPATH (where you want the finished .objs to go)
 - SCIPTS_FILEPATH (Where you want the individual combo scripts)
 - SCRIPT_MANAGER_ALL_FILEPATH (where you want the batch/all script)
 - SCRIPT_MANAGER_SOME_FILEPATH (where you want the batch/some script)

When running the Object Compiler, the app will cycle through the created scripts, and create a single batch script that cant be run inside your 3DS Max software to generate the actual objects.  
