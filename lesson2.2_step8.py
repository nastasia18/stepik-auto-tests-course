import time
import os
from selenium import webdriver

try:
    # Открыть страницу в браузере
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Заполнить имя, фамилию, е-маил
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Smirnov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("aaa@aa")

    # Загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Узнать к путь текущей директории
    file_path = os.path.join(current_dir, 'file.txt')  # Указать путь к файлу, который находится в текущей директории
    file_btn = browser.find_element_by_css_selector("#file")
    file_btn.send_keys(file_path)  # Добавить этот файл

    # Нажать на кнопку Submit
    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
