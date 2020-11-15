from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config
import login

def main():
    chrome_options = Options()
    chrome_options.binary_location = config.CHROMIUM_PATH
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH, options=chrome_options)

    driver.get('https://myst.mcth.ir/login.aspx')

    login.login_to_site(driver)
    login.open_amar_page(driver)

if __name__ == "__main__":
    main()
