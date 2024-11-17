from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import time
from config import DATE_FILE
import algorithms

eghamat_min, eghamat_max, vorod_min, vorod_max, khoroj_min, khoroj_max, otagh_min, otagh_max = algorithms.choose_rand()

def register_amar(driver):
    """ثبت آمار در سایت."""
    count = 0
    while True:
        try:
            wait = driver(driver, 10000)
            element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnk_register"))) 
            element.click() 
            with open(DATE_FILE) as file: 
                lines = file.readlines()  
                if count < len(lines):  
                    line = lines[count].strip()  
                else:
                    break  
            
            # random values
            # اگر مقدار رندوم برابر با رندوم بود از فانکشن رندوم مقادیر رو بگیر و ریترن کن
            
            eghamat_random, vorod_random, khoroj_random, otagh_random = algorithms.random_numbers(
            eghamat_min=1,
            eghamat_max=10,
            vorod_min=1,
            vorod_max=5,
            khoroj_min=2,
            khoroj_max=7,
            otagh_min=3,
            otagh_max=9
            )

            # Set values for foreign entries
            time.sleep(1)
            input_element_4 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[2]/input')))
            input_element_4.clear()   
            input_element_4.send_keys('0')
            
            input_element_5 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[9]/div[1]/input')))
            input_element_5.clear()   
            input_element_5.send_keys('0')
            
            input_element_6 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[9]/div[2]/input')))
            input_element_6.clear()   
            input_element_6.send_keys('0')
            time.sleep(1)
            
            # Set values for Iranian entries
            input_element_1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[1]/input')))
            input_element_1.clear()   
            input_element_1.send_keys(eghamat_random)
            
            input_element_2 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[1]/input')))
            input_element_2.clear() 
            input_element_2.send_keys(vorod_random)
            
            input_element_3 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[2]/input')))
            input_element_3.clear() 
            input_element_3.send_keys(khoroj_random)
            
            # Set values for room entries
            input_element_7 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[3]/input')))
            input_element_7.clear() 
            input_element_7.send_keys(otagh_random)
            time.sleep(1)
            
            # Set date value
            input_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[3]/div/input')))
            input_element.clear()   
            input_element.send_keys(line)  
            time.sleep(3)
            
            # Submit the form
            submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[3]/input[1]')))
            submit_element.click()
            
            # Close the registration page
            close_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div[2]/div/input')))
            close_element.click()
            print(line)
            count += 1

            # wait for new sabt
            time.sleep(2)

            # add error lines to date file to sabt them again
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            with open(DATE_FILE, 'a') as file_to_write:
                file_to_write.write(line + '\n')
            continue

