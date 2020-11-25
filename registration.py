from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import algorithms
from config import DATE_FILE



def register_amar(driver):
    count = 0
    while True:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnk_register")))
        element.click()

        with open(DATE_FILE) as file:
            lines = file.readlines()
            if count < len(lines):
                line = lines[count].strip()
            else:
                break

        eghamat_random, vorod_random, khoroj_random, otagh_random = algorithms.random_numbers(
            eghamat_min=1, eghamat_max=10,
            vorod_min=1, vorod_max=5,
            khoroj_min=2, khoroj_max=7,
            otagh_min=3, otagh_max=9,
        )

        input_element_1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[1]/input')))
        input_element_1.clear()
        input_element_1.send_keys(eghamat_random)

        input_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[3]/div/input')))
        input_element.clear()
        input_element.send_keys(line)
        time.sleep(2)

        submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[3]/input[1]')))
        submit_element.click()
        print(line)
        count += 1
        time.sleep(2)
