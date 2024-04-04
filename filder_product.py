from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def create_product_with_mark(admin_username, admin_password, product_data, admin_url, driver_path):
    # راه‌اندازی مرورگر و باز کردن صفحه ورود
    driver = webdriver.Edge(executable_path=driver_path)
    driver.get(admin_url)

    # ورود اطلاعات کاربری
    username_field = driver.find_element_by_id("id_username")
    password_field = driver.find_element_by_id("id_password")
    username_field.send_keys(admin_username)
    password_field.send_keys(admin_password)
    password_field.send_keys(Keys.RETURN)

    # تأیید ورود
    login_button = driver.find_element_by_css_selector("input[type='submit']")
    login_button.click()

    # حرکت به صفحه ایجاد محصول
    driver.get(admin_url + "your_app_name/product/add/")

    # وارد کردن اطلاعات محصول
    name_field = driver.find_element_by_id("id_name")
    name_field.send_keys(product_data['name'])

    description_field = driver.find_element_by_id("id_description")
    description_field.send_keys(product_data['description'])

    price_field = driver.find_element_by_id("id_price")
    price_field.send_keys(str(product_data['price']))

    # انتخاب مارک از لیست
    mark_dropdown = Select(driver.find_element_by_id("id_mark"))
    mark_dropdown.select_by_visible_text(product_data['mark'])

    category_field = driver.find_element_by_id("id_category")
    for category_name in product_data['categories']:
        category_field.send_keys(category_name)
        category_field.send_keys(Keys.RETURN)

    img_field = driver.find_element_by_id("id_img")
    img_field.send_keys(product_data['img_path'])

    discount_field = driver.find_element_by_id("id_discount")
    discount_field.send_keys(str(product_data['discount']))

    discounted_price_field = driver.find_element_by_id("id_discounted_price")
    discounted_price_field.send_keys(str(product_data['discounted_price']))

    inventory_range_field = driver.find_element_by_id("id_inventory_range")
    inventory_range_field.send_keys(str(product_data['inventory_range']))

    inventory_field = driver.find_element_by_id("id_inventory")
    if product_data['inventory']:
        inventory_field.click()

    # ذخیره محصول
    save_button = driver.find_element_by_css_selector("input[name='_save']")
    save_button.click()

    # حتماً مرورگر را ببندید پس از اتمام کار
    time.sleep(2)  # انتظار برای مطمئن شدن از ذخیره شدن محصول
    driver.quit()


# اجرای تابع برای ایجاد محصولات با مارک‌های مختلف
products_data = [
    {
        'name': 'محصول 1',
        'description': 'توضیحات محصول 1',
        'price': 20000,
        'categories': ['دسته‌بندی 1', 'دسته‌بندی 2'],
        'img_path': '/path/to/image1.jpg',
        'discount': 10,
        'discounted_price': 18000,
        'mark': 'مارک 1',
        'inventory_range': 100,
        'inventory': True
    },
    {
        'name': 'محصول 2',
        'description': 'توضیحات محصول 2',
        'price': 30000,
        'categories': ['دسته‌بندی 2', 'دسته‌بندی 3'],
        'img_path': '/path/to/image2.jpg',
        'discount': 20,
        'discounted_price': 24000,
        'mark': 'مارک 2',
        'inventory_range': 50,
        'inventory': False
    }
]

for product_data in products_data:
    create_product_with_mark("نام_کاربری_ادمین", "رمز_عبور_ادمین", product_data, "http://آدرس-ادمین-جنگو.com/admin/", "مسیر_تا_فایل_اجرایی_مرورگر_ایج")
