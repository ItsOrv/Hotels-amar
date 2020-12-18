def choose_date_file():
    choice = input("Do you want to use existing date.txt file? (y/n) ").strip().lower()
    if choice == "y":
        return
    elif choice == "n":
        return
    else:
        print("wrong answer")
        return choose_date_file()
