import random
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta

# تعداد روزهای هر ماه شمسی
days_in_month = {
    1: 31, 2: 31, 3: 31, 4: 30, 5: 30, 6: 30,
    7: 30, 8: 30, 9: 30, 10: 30, 11: 29, 12: 29  # در نظر گرفتن سال غیر کبیسه
}

# تابع تولید تاریخ‌های شمسی
def generate_dates(start_date, end_date):
    current_date = datetime.strptime(start_date, "%Y/%m/%d")
    end_date = datetime.strptime(end_date, "%Y/%m/%d")
    dates = []

    while current_date <= end_date:
        dates.append(current_date.strftime("%Y/%m/%d"))
        current_date += timedelta(days=1)

    return dates

# تابع توزیع تصادفی اعداد با مجموع مشخص در یک ماه
def distribute_random(total, days, min_value, max_value):
    distributed = []
    
    for i in range(days - 1):
        value = random.randint(min_value, max_value)
        distributed.append(value)
        total -= value

    distributed.append(total)

    if any(value < min_value or value > max_value for value in distributed):
        return distribute_random(sum(distributed), days, min_value, max_value)

    return distributed

# مقادیر کلی هر متغیر در هر ماه
monthly_totals = {
    'eghamat': {1: 400, 2: 350, 3: 248, 4: 390, 5: 310, 6: 370, 7: 410, 8: 430, 9: 360, 10: 320, 11: 280, 12: 260},
    'vorod': {1: 200, 2: 180, 3: 160, 4: 190, 5: 150, 6: 170, 7: 210, 8: 220, 9: 180, 10: 160, 11: 140, 12: 130},
    'khoroj': {1: 180, 2: 160, 3: 140, 4: 170, 5: 130, 6: 150, 7: 190, 8: 200, 9: 160, 10: 140, 11: 120, 12: 110},
    'otagh': {1: 100, 2: 90, 3: 80, 4: 110, 5: 70, 6: 90, 7: 120, 8: 130, 9: 100, 10: 90, 11: 80, 12: 70},
}

# تولید مقادیر برای هر تاریخ
def generate_data(start_date, end_date):
    dates = generate_dates(start_date, end_date)
    data = []

    for date in dates:
        year, month, day = map(int, date.split('/'))

        days_in_current_month = days_in_month[month]

        # توزیع تصادفی اعداد برای هر روز
        random_eghamat = distribute_random(monthly_totals['eghamat'][month], days_in_current_month, 5, 20)
        random_vorod = distribute_random(monthly_totals['vorod'][month], days_in_current_month, 5, 20)
        random_khoroj = distribute_random(monthly_totals['khoroj'][month], days_in_current_month, 5, 20)
        random_otagh = distribute_random(monthly_totals['otagh'][month], days_in_current_month, 5, 20)

        data.append({
            'date': date,
            'eghamat': random_eghamat[int(day)-1],
            'vorod': random_vorod[int(day)-1],
            'khoroj': random_khoroj[int(day)-1],
            'otagh': random_otagh[int(day)-1]
        })

    return data

# تابع اصلی
def main():
    # تنظیمات Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  #(امیدوارم) جلوگیری از بسته شدن مرورگر
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # صفحه ورود
    driver.get('https://myst.mcth.ir/login.aspx')
    email_input = input('email: ')
    email_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    email_input_field.send_keys(email_input)

    number_input = input('number: ')
    number_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/input')))
    number_input_field.send_keys(number_input)

    captcha_input = input('captcha: ')
    captcha_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[3]/input')))
    captcha_input_field.send_keys(captcha_input)

    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[5]/input')))
    submit_button.click()

    # صبر برای ورود
    time.sleep(6)

    # وارد کردن کد
    code_input = input('code: ')
    code_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    code_input_field.send_keys(code_input)

    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div[1]/input')))
    login_button.click()

    # رفتن به صفحه آمار
    time.sleep(6)
    driver.execute_script("window.open('https://myst.mcth.ir/eghamat_amar_daily.aspx', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])
    driver.execute_script("window.history.go(0)")
    time.sleep(6)

    # تولید داده‌های تاریخ‌ها و مقادیر
    start_date = "1402/03/03"
    end_date = "1402/08/01"
    data = generate_data(start_date, end_date)

    # وارد کردن مقادیر در سایت
    for entry in data:
        try:
            wait = WebDriverWait(driver, 10000)
            element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnk_register"))) 
            element.click()

            time.sleep(1)
            # وارد کردن مقادیر تصادفی
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[1]/input'))).send_keys(entry['eghamat'])
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[1]/input'))).send_keys(entry['vorod'])
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[2]/input'))).send_keys(entry['khoroj'])
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[3]/input'))).send_keys(entry['otagh'])
            time.sleep(1)
        except Exception as e:
            print(f"Error on date {entry['date']}: {e}")

if __name__ == "__main__":
    main()
