from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def sum_num(x, y):
    return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    val = sum_num(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(val)

    button = browser.find_element_by_css_selector(".btn")
    button.click()



finally:
    time.sleep(5)
    browser.quit()
