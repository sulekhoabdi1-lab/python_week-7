shopping_list = []

while True:
    choice = input("Enter command (add / remove / show / done): ").strip().lower()
   
    if choice == "add":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added.")
    elif choice == "remove":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print("That item is not on your list.")
    elif choice == "show":
        print("Current Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    elif choice == "done":
        print("Goodbye! Have a great day.")
        break
    else:
        print("Invalid command. Please try again (add / remove / show / done).")
