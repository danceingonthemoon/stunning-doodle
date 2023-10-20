shopping_trolley = {"Fruits": ["apple", "banana", "blueberry", "strawberry", "raseperry"], "Food": [
    "soy_milk", "bread", "lettuce", "butter"], "Drinks": ["water", "coca_cola", "beer"]}

shopping_list = {}

# Assign IDs to the items


def display_items():
    cate_id = 000
    for category, items in shopping_trolley.items():
        cate_id += 100
        print(f"{cate_id} ------------ {category}\n")

        item_id = 0
        for item in items:
            item_id += 1
            print(f"{cate_id+item_id}--{item}\n")


def display_shopping_list():
    print("\n---------------------My shopping List-----------------------\n")
    for item, quantity in shopping_list.items():
        print(f"------{item} :  {quantity}")


def add_to_trolley():

    # for category in shopping_trolley:
    #     if item in category:
    #         print(f"{item} is already in the shopping trolley.\n")
    #         return
    # print("The item is not in the shopping trolley. You can add it to an existing category or create a new category.\n")
    category_name = input(
        "Enter the category name or choose an existing category:\n ")
    new_item = input("Enter the item for this category:\n")
    for category in shopping_trolley:
        # Assuming the category name is the first item in the list
        if category_name.lower() == category.lower():
            category.append(new_item)
            print(
                f"{item} has been added to the shopping trolley in the '{category_name}' category.\n")
            return
    print(
        f"No such category '{category_name}' exists. Creating a new category.")
    shopping_trolley.append([category_name, new_item])
    print(f"{new_item} has been added to the shopping trolley in the new '{category_name}' category.")


def buy_items():
    display_items()
    item = input("\nWhat you want to buy : \n").lower()
    purchased_quantity = 0
    check = False
    for category, items in shopping_trolley.items():
        for shopping_item in items:
            if item == shopping_item:
                check = True
                break

    if check:
        purchased_quantity = int(input("How much you want to buy : \n"))
        if purchased_quantity > 0:
            if item in shopping_list:
                shopping_list[item] += purchased_quantity
            else:
                shopping_list[item] = purchased_quantity
            print(
                f"Thanks for shopping with us. You bought {purchased_quantity} of {item} today. \n")
            display_shopping_list()
        else:
            print(f"Invalid quantity.")
    else:
        add_to_trolley()
        # print("Invalid item selection. Please choose from the available items.")


def remove_items_of_shopping_list():
    # display_shopping_list()
    remove_item = input("Remove the items : ").lower()
    if remove_item in shopping_list:
        del shopping_list[remove_item]
        print(f"{remove_item}  already removed from the shopping list.")
    else:
        print(f"{remove_item} are not found in the shopping list.")


try:
    key_list = {"d": "Display items", "a": "Add items",
                "b": "Buy itmes", "s": "Show your shopping list", "r": "Remove items"}
    key_press = False
    while not (key_press == "q"):
        print("\n---------------------Welcome to Coco Grocery---------------------\n")
        for key, value in key_list.items():
            print("\nPress", key, "To", value)
        user_input = input("\nEnter your options :  \n").lower()
        if user_input == "d":
            print("Current selection: display items in the shopping trolley\n")
            display_items()
        elif user_input == "a":
            print("Current selection: add to trolley\n")
            item = ""
            add_to_trolley(item)
        elif user_input == "b":
            print("Current selection: buy items\n")
            buy_items()
        elif user_input == "s":
            print("Current selection: show your shopping items\n")
            display_shopping_list()
        elif user_input == "r":
            print("Current selection: remove items from the shopping list\n")
            remove_items_of_shopping_list()
        elif user_input == "q":
            break
        else:
            continue
except Exception as e:
    print("Invalid input. Please enter a valid option.\n")
finally:
    print("Execution completed.")
