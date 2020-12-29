def choose_date_file():
    """
    انتخاب استفاده از فایل date.txt یا شروع اسکرپر تاریخ.
    """
    choice = input(r"choose an option: \n Do you want to use existing date.txt file? (y/n)").strip().lower()
    if choice == "y":
        return True
    if choice == "n":
        return False
    print("wrong answer")
    return choose_date_file()  # ask again



