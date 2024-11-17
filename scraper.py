from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def choose_date_file():
    """
    انتخاب استفاده از فایل date.txt یا شروع اسکرپر تاریخ.
    """
    choice = input(r"choose an option: \n Do you want to use existing date.txt file? (y/n)").strip().lower()
    if choice == "y": 
        method = "rand"
        return
    if choice == "n":
        method = "trand"
        return
    else:
        print("wrong answer")
        return choose_date_file() # ask again



