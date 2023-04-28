menu_dict = {
    "pizza": 199,
    "bread": 200,
    "burger": 100
}

menu = input("Enter menu : ")
if (menu in menu_dict.keys()): 
    print(f"Menu : {menu} , Price : {menu_dict[menu]}")
else:
    print("We don't have any matching menu")

#OUTPUT
"""
Enter menu : pizza
Menu : pizza , Price : 199
"""