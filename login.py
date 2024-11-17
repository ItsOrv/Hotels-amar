from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_site(driver):
    try:
        # Email
        email_input = input('Input email: ')
        email_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
        email_input_field.send_keys(email_input)

        # Number
        number_input = input('Input number: ')
        number_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/input')))
        number_input_field.send_keys(number_input)

        # Captcha
        captcha_input = input('Input captcha: ')
        captcha_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[3]/input')))
        captcha_input_field.send_keys(captcha_input)
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[5]/input')))
        submit_button.click()

        time.sleep(6)

        # Code
        code_input = input('Input code: ')
        code_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
        code_input_field.send_keys(code_input)
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div[1]/input')))
        login_button.click()

        time.sleep(6)
    except Exception as e:
        raise Exception(f"Login failed: {e}")

def open_amar_page(driver):
    try:
        # amar page
        driver.execute_script("window.open('https://myst.mcth.ir/eghamat_amar_daily.aspx', '_blank')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.execute_script("window.history.go(0)")
        time.sleep(6)
    except Exception as e:
        raise Exception(f"Going to amar page failed: {e}")

