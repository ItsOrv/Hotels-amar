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

# month
days_in_month = {
    1: 31, 2: 31, 3: 31, 4: 31, 5: 31, 6: 31,
    7: 30, 8: 30, 9: 30, 10: 30, 11: 30, 12: 29
}

# generage dates
def generate_dates(start_date, end_date):
    current_date = datetime.strptime(start_date, "%Y/%m/%d")
    end_date = datetime.strptime(end_date, "%Y/%m/%d")
    dates = []
    while current_date <= end_date:
        dates.append(current_date.strftime("%Y/%m/%d"))
        current_date += timedelta(days=1)
    return dates
    
# rand in range
def distribute_random(total, days, min_value, max_value):
    distributed = []
    if days * min_value > total or days * max_value < total:
        raise ValueError("Cannot distribute the values within the given bounds.")
    if days == 1:
        distributed.append(total)
        return distributed
    for i in range(days - 1):
        max_possible_for_day = total - (days - len(distributed) - 1) * min_value
        min_possible_for_day = min_value
        value = random.randint(min_possible_for_day, min(max_value, max_possible_for_day))
        distributed.append(value)
        total -= value
    distributed.append(total)
    return distributed

# total in month
monthly_totals = {
    'eghamat': {1: 1140, 2: 930, 3: 900, 4: 820, 5: 750, 6: 1740, 7: 1500, 8: 430, 9: 360, 10: 320, 11: 280, 12: 260},
    'vorod': {1: 1140, 2: 930, 3: 900, 4: 824, 5: 751, 6: 1748, 7: 210, 8: 220, 9: 180, 10: 160, 11: 140, 12: 130},
    'khoroj': {1: 1100, 2: 900, 3: 990, 4: 817, 5: 739, 6: 1737, 7: 190, 8: 200, 9: 160, 10: 140, 11: 120, 12: 110},
    'otagh': {1: 380, 2: 310, 3: 300, 4: 280, 5: 250, 6: 580, 7: 500, 8: 130, 9: 100, 10: 90, 11: 80, 12: 70},
}

#generate full data
def generate_data(start_date, end_date):
    dates = generate_dates(start_date, end_date)
    data = []
    for date in dates:
        year, month, day = map(int, date.split('/'))
        days_in_current_month = days_in_month[month]
        random_eghamat = distribute_random(monthly_totals['eghamat'][month], days_in_current_month, 12, 77)
        random_vorod = distribute_random(monthly_totals['vorod'][month], days_in_current_month, 12, 77)
        random_khoroj = distribute_random(monthly_totals['khoroj'][month], days_in_current_month, 12, 77)
        random_otagh = distribute_random(monthly_totals['otagh'][month], days_in_current_month, 4, 26)
        data.append({
            'date': date,
            'eghamat': random_eghamat[int(day)-1],
            'vorod': random_vorod[int(day)-1],
            'khoroj': random_khoroj[int(day)-1],
            'otagh': random_otagh[int(day)-1]
        })
    return data

start_date = "1403/01/01"
end_date = "1403/06/22"
data = generate_data(start_date, end_date)
print(data)

# main
def main():
    # Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # open page and input
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
    time.sleep(6)
    # code
    code_input = input('code: ')
    code_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    code_input_field.send_keys(code_input)
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div[1]/input')))
    login_button.click()
    # amar page
    time.sleep(6)
    driver.execute_script("window.open('https://myst.mcth.ir/eghamat_amar_daily.aspx', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])
    driver.execute_script("window.history.go(0)")
    time.sleep(6)
    # start and end date
    start_date = "1403/01/01"
    end_date = "1403/06/22"
    data = generate_data(start_date, end_date)

    # main loop
    for entry in data:
        try:
            wait = WebDriverWait(driver, 10000)
            element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnk_register"))) 
            element.click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[1]/input'))).send_keys(entry['eghamat'])
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[1]/input'))).send_keys(entry['vorod'])
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[2]/input'))).send_keys(entry['khoroj'])
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[3]/input'))).send_keys(entry['otagh'])
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[2]/input'))).send_keys("0")
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[9]/div[1]/input'))).send_keys("0")
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[9]/div[2]/input'))).send_keys("0")
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[3]/div/input'))).clear()
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[3]/div/input'))).send_keys(entry['date'])
            #sabt
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[3]/input[1]'))).click()
            #close (sabt page)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div[2]/div/input'))).click()
            time.sleep(1)
        except Exception as e:
            print(f"Error on date {entry['date']}: {e}")

if __name__ == "__main__":
    main()
