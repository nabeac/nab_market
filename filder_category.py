from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def create_category(admin_username, admin_password, new_category_name, admin_url, driver_path):
    # راه‌اندازی مرورگر و باز کردن صفحه ورود
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(admin_url)

    # ورود اطلاعات کاربری
    username_field = driver.find_element_by_id("aryan")
    password_field = driver.find_element_by_id("13871387")
    username_field.send_keys(admin_username)
    password_field.send_keys(admin_password)
    password_field.send_keys(Keys.RETURN)

    # تأیید ورود
    login_button = driver.find_element_by_css_selector("input[type='submit']")
    login_button.click()

    # حرکت به صفحه ایجاد دسته‌بندی
    driver.get(admin_url + "market/category/add/")

    # وارد کردن اطلاعات دسته‌بندی جدید
    category_name_field = driver.find_element_by_id("id_name")
    category_name_field.send_keys(new_category_name)

    # ذخیره دسته‌بندی جدید
    save_button = driver.find_element_by_css_selector("input[name='_save']")
    save_button.click()

    # حتماً مرورگر را ببندید پس از اتمام کار
    time.sleep(2)  # انتظار برای مطمئن شدن از ذخیره شدن دسته‌بندی
    driver.quit()


# اجرای تابع برای ایجاد دسته‌بندی‌های مختلف
categories = ["موبایل", "کنسول بازی", "لپ تاپ", "کامپیوتر", "گیمینگ", "cpu"]  # نام‌های دسته‌بندی مختلف
for category in categories:
    create_category("your_admin_username", "your_admin_password", category, "http://127.0.0.1/admin/", "msedgedriver.exe")
