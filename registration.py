from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def register_amar(driver):
    count = 0
    while True:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnk_register")))
        element.click()
        count += 1
        time.sleep(2)
