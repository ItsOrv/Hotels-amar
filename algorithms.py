import random

def random_numbers(eghamat_min, eghamat_max, vorod_min, vorod_max, khoroj_min, khoroj_max, otagh_min, otagh_max):
    """
    تولید مقادیر تصادفی بر اساس مینیمم و ماکزیمم داده شده.
    """
    eghamat_random = random.randint(eghamat_min, eghamat_max)
    vorod_random = random.randint(vorod_min, vorod_max)
    khoroj_random = random.randint(khoroj_min, khoroj_max)
    otagh_random = random.randint(otagh_min, otagh_max)
    print(f"اعداد تصادفی تولید شدند:")    
    return eghamat_random, vorod_random, khoroj_random, otagh_random


def distribute_random_numbers():
    """توزیع تصادفی اعداد در ماه."""
    # TODO: کد مربوطه را اینجا اضافه کنید.
    pass

def auto_detect_numbers():
    """تشخیص خودکار اعداد."""
    # TODO: کد مربوطه را اینجا اضافه کنید.
    pass


def choose_rand():
    """
    انتخاب روش تولید اعداد تصادفی       
    """
    choice = input(r"choose an option: 1- generate simple random number in range. \n2- generate Random distribution of random numbers in a certain range in the fixed sum of the month (1/2)").strip().lower()
    if choice == "1": 
        method = "rand"
        eghamat_min = input("Enter eghamat min: ")
        eghamat_max = input("Enter eghamat maz: ")
        vorod_min = input("Enter vorod min: ")
        vorod_max = input("Enter vorod max: ")
        khoroj_min = input("Enter khoroj min: ")
        khoroj_max = input("Enter khoroj max: ")
        otagh_min = input("Enter otagh min: ")
        otagh_max = input("Enter otagh max: ")
        return eghamat_min, eghamat_max, vorod_min, vorod_max, khoroj_min, khoroj_max, otagh_min, otagh_max
    if choice == "2":
        method = "norand"
        auto_detect_numbers()
        return method
    else:
        print("wrong answer")
        return choose_rand() # ask again
