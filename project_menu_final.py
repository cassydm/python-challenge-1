# SECTION 1: MENU DEFINING

# defining name and menu dictionary
name = "Cassy's Baked Potato Bar"
menu = {
    "Baked Potatoes":{
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

# SECTION 2: ORDERING LOOP

# Order looping sequence
# Creating dict for item orders
order_dict = []
# Begin taking order
place_order = True
while place_order:
    # Take initial order from category selection
    print("From which menu would you like to order?")
    # Setting the counter to 1 and defining the order dictionary
    i = 1
    menu_items = {}
    # Printing options to choose from
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    # Get the customer's input
    menu_category = input("Which menu number would you like to order from?: ")
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            section_break = "=" * 42
            section_break2 = " " * 42
            print(section_break)
            spacing = "-------|--------------------------|-------"
            print(f"You are viewing the {menu_category_name} menu")
            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print(section_break2)
            print(menu_category_name)
            print(spacing)
            print("Item # | Item name                | Price")
            print(spacing)
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
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
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            print(spacing)
            #entering new loop to begin taking item order detail to put into
            #previously defined dict
            item_order = True
            while item_order:
                print(section_break2)
                #user input
                item_selection = input("Which item number would you like to order?")
                # Validate input is int. 
                # If int, then check if in sub menu 
                if item_selection.isdigit():
                    item_selection = int(item_selection)
                    if item_selection in menu_items.keys():
                        # Store the values as variables
                        item_selection_name = menu_items[item_selection]['Item name']
                        item_selection_price = menu_items[item_selection]['Price']
                        # Ask for quantity
                        item_qty = input(f"How many {item_selection_name} {menu_category_name} would you like?")
                        # Check if valid qty number or set to 1
                        if item_qty.isdigit():
                            item_qty = int(item_qty)
                        else:
                            item_qty = 1
                        # Print selection
                            # Total cost
                        total_cost = item_qty * item_selection_price
                        print(f"You ordered {item_qty} {item_selection_name} for ${item_selection_price:.2f} each.")
                        print(f"Total: ${total_cost:.2f}") #print validation
                        # Store in dict by appending
                        order_dict.append({
                            "Item Name": item_selection_name,
                            "Price": item_selection_price,
                            "Qty": item_qty
                        })
                        #print(order_dict) place holder print to view if inputs were stored correctly
                        # Break out of this while loop 
                        break
                    # If number isn't in dict
                    else:
                        print("Invalid menu item. Try Again")
                # If not number
                else:
                    print("Invalid input. Try again")
                    break
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
    #enter the keep ordering loop
    while True:
        #creating the input and ensuring "y" is always counted correctly
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o.")
        keep_ordering = keep_ordering.upper()
        #if yes, break out of this while loop
        if keep_ordering == "Y":
            break
        else:
            #if no, or else, break out of this loop, and the 
            #ordering sequence loop
            place_order = False
            break

# SECTION 3: FINAL ORDER TICKET OUTPUT
#final print reciept sequence
print(section_break)
print(f"       Thank you for ordering from \n        {name}")
print("   This is what we are prepping for you:")
print(spacing)
print(" Qty   | Item name                | Price")
print(spacing)
#setting i to 1
i = 1
#grand total def
grand_total=0
#looping each item ordered in the dictionary
for item in order_dict:
    #define variables
    item_name = item['Item Name']
    item_qty = item['Qty']
    item_price = item['Price']
    total_item=item_price * item_qty
    num_spaces_total= 24 - len(item_name) - 3
    grand_total+=total_item
    #string width formating to ensure formatting does not break 
    #no matter the inputs 
    print(f"  {item_qty:<5}| {item_name:<25}| ${total_item:.2f}")
    i += 1
print(spacing)
print(f" Total |                          | ${grand_total:.2f}")
print(spacing)
print(section_break)