from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидание снижении цены
    val = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_css_selector("#book")
    button.click()

    # Решение примера
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    ans = calc(x)

    # Запись в поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(ans)

    # Нажать кнопку для отправки ответа
    btn = browser.find_element_by_css_selector("#solve")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
