#Baked Potato Food Truck Menu
name = "Cassy's Baked Potato Bar"
menu = {
    "Baked Potatoes": {
        "Original": 6.50,
        "Loaded": 8.00,
        "Chili": 10.50,
        "Taco": 10.50
        },       
    "Add ins":{
        "Extra Cheese": 1.00,
        "Extra Sour Cream": 1.00,
        "Extra Butter": 0.50,
        "Bacon": 1.50,
        "Chives": 0.50,
        "Nacho Cheese": 2.00,
        "Guacamole": 2.00,
        "Hot Sauce": 1.00,
        "Jalepenos": 0.50,
        },
    "Desserts": {
        "Sweet Potato": 8.50,
        "Cookie":{
            "Chocolate Chip": 3.00,
            "Peanutbutter": 3.00,
            "Snickerdoodle": 4.00
            }
        },
    "Drinks": {
        "Water": 1.00,
        "Lemonade": 2.50,
        "Soda": {
            "Pepsi": 2.50,
            "Mountain Dew": 2.50,
            "Root Beer": 2.50,
            "Dr. Pepper": 2.50,
        },
        "Iced Tea": 3.00
    }        
}

#Welcome message
print(f"Welcome to {name}!")

#Begin order loop
place_order=True
while place_order:
    print()
    print("Which category would you like to order from?")
    #Menu item order counter
    i = 1
    #menu order storage dictionary
    menu_items={}
    #Choose from headings and store selection
    for key in menu.keys():
        print(f"{i}:{key}")
        menu_items[i] = key
        i += 1
    #Getting customer input
    menu_category = input("Please select the category number: ")
    #validation check
    if menu_category.isdigit():
        #first if check to validate if valid number.
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            #if yes, then prompt customer what menu item to order
            print(f"You selected {menu_category_name}")
            #Menu options
            print(f"What {menu_category_name} item would you like to order?")
            #menu print
            i = 1
            menu_items = {}
            print("Item # | Item Name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                #checking for dictionaries
                if type(value) is dict:
                    #if dictionary loop through and print items in menu category
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | "
                          + f"{key}{item_spaces} | ${value:.2f}")
                    # Add 1 to the item_counter
                    i += 1
            print("-------|--------------------------|-------")
            input("Press enter to return to the main menu.")