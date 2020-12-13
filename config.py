import os

# تنظیمات مربوط به مرورگر و درایورها
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
CHROMIUM_PATH = "/usr/bin/google-chrome-stable"

# تنظیمات مسیر فایل‌ها
DATE_FILE = os.path.join(os.getcwd(), "date.txt")
LOG_FILE = os.path.join(os.getcwd(), "logs", "app.log")

# تنظیمات پیش‌فرض
DEFAULT_WAIT_TIME = 10  # زمان انتظار پیش‌فرض برای WebDriver
