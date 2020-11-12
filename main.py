from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import login

CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
CHROMIUM_PATH = "/usr/bin/google-chrome-stable"

chrome_options = Options()
chrome_options.binary_location = CHROMIUM_PATH
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)

driver.get('https://myst.mcth.ir/login.aspx')

login.login_to_site(driver)
