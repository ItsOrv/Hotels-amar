# Import statements sorted
import random
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#9111
#5799884541
#____________________________________________________
def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # برای جلوگیری از بسته شدن کروم
#___login page_______________________________________
    driver.get('https://myst.mcth.ir/login.aspx')
    email_input = input('email: ')
    email_input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    email_input_field.send_keys(email_input)
    number_input = input('number: ')
    number_input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/input')))
    number_input_field.send_keys(number_input)
    captcha_input = input('capcha:')
    captcha_input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[3]/input')))
    captcha_input_field.send_keys(captcha_input)
    submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[5]/input')))
    submit_button.click()
    #wait
    time.sleep(6)
    code_input = input('code:')
    code_input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    code_input_field.send_keys(code_input)
    login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div[1]/input')))
    login_button.click()
    #wait
    time.sleep(6)
#___amar page________________________________________
    driver.execute_script("window.open('https://myst.mcth.ir/eghamat_amar_daily.aspx', '_blank')")
    driver.switch_to.window(driver.window_handles[-1])
    driver.execute_script("window.history.go(0)")
    #wait
    time.sleep(6)
#___sabt jadid_______________________________________
    date_file = "/home/orb/Documents/amar/date.txt"
    count = 0
    while True:
        try:
            wait = WebDriverWait(driver, 10000)
            element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnk_register"))) 
            element.click() 
            with open(date_file) as file: 
                lines = file.readlines()  
                if count < len(lines):  
                    line = lines[count].strip()  
                else:
                    break  
            #randoms
            random_number_eghamat = random.randint(10, 26)
            random_number_vorod = random.randint(4, 10)
            random_number_khoroj = random.randint(4, 10)
            random_number_otagh = random.randint(2, 8)
            #kharej
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
            #irani
            input_element_1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[1]/input')))
            input_element_1.clear()   
            input_element_1.send_keys(random_number_eghamat)
            input_element_2 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[1]/input')))
            input_element_2.clear() 
            input_element_2.send_keys(random_number_vorod)
            input_element_3 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[7]/div[2]/input')))
            input_element_3.clear() 
            input_element_3.send_keys(random_number_khoroj)
            #otagh
            input_element_7 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[4]/div[3]/input')))
            input_element_7.clear() 
            input_element_7.send_keys(random_number_otagh)
            time.sleep(1)
            #tarikh
            input_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/div/div[3]/div/input')))
            input_element.clear()   
            input_element.send_keys(line)  
            time.sleep(3)
            #sabt
            submit_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div/div[9]/div[2]/div[3]/div/div[1]/div/div[3]/div[3]/input[1]')))
            submit_element.click()
            #close (sabt page)
            close_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div[2]/div/input')))
            close_element.click()
            print(line)
            count += 1
            time.sleep(1)
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            with open(date_file, 'a') as file_to_write:
                file_to_write.write(line + '\n')
            continue
if __name__ == '__main__':
    main()
