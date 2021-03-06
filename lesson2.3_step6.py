from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажать на кнопку
    btn = browser.find_element_by_css_selector(".btn")
    btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Решаем пример
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    val = calc(x)

    # Записываем ответ в поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(val)

    # Нажимаем на кнопку для отправки ответа
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()