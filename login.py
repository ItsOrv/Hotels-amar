from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_to_site(driver):
    email_input = input('Input email: ')
    email_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    email_input_field.send_keys(email_input)

    number_input = input('Input number: ')
    number_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/input')))
    number_input_field.send_keys(number_input)

    captcha_input = input('Input captcha: ')
    captcha_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[4]/input')))
    captcha_input_field.send_keys(captcha_input)
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[5]/input')))
    submit_button.click()

    time.sleep(6)

    code_input = input('Input code: ')
    code_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    code_input_field.send_keys(code_input)
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/div[1]/input')))
    login_button.click()

    time.sleep(6)
