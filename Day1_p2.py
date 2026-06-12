phone_book = {}

while True:
    print("\n1.Add")
    print("2.Search")
    print("3.Remove")
    print("4.View All")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone: ")
        phone_book[name] = number

    elif choice == "2":
        name = input("Search name: ")
        print(phone_book.get(name, "Not Found"))

    elif choice == "3":
        name = input("Remove name: ")
        phone_book.pop(name, None)

    elif choice == "4":
        print(phone_book)

    elif choice == "5":
        break