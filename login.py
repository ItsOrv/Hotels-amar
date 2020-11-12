from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_to_site(driver):
    email_input = input('Input email: ')
    email_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[1]/input')))
    email_input_field.send_keys(email_input)

    number_input = input('Input number: ')
    number_input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[4]/div/div[3]/div[2]/div/div/div[2]/input')))
    number_input_field.send_keys(number_input)
