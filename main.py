from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import algorithms
import config
import login
import scraper
import registration

def main():
    # تنظیمات مرورگر
    chrome_options = Options()
    chrome_options.binary_location = config.CHROMIUM_PATH
    chrome_options.add_experimental_option("detach", True)

    # ایجاد WebDriver
    service = ChromeService(executable_path=config.CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # باز کردن صفحه ورود
    driver.get('https://myst.mcth.ir/login.aspx')
    
    # ورود به سیستم
    login.login_to_site(driver)

    #  دریافت اطلاعات ثبت نشده از فایل یا اسکرپینگ
    scraper.choose_date_file(driver)

    

    # رفتن به صفحه ثبت امار
    login.open_amar_page(driver)

    # انتخاب روش ساخت اعداد رندوم
    # شروع ثبت 
    registration.sabt()

if __name__ == "__main__":
    main()
