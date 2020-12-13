from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    ans = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(ans)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkBox = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
    checkBox.click()

    radio = browser.find_element_by_css_selector("[for = 'robotsRule']")
    radio.click()

    button.click()
finally:
    time.sleep(10)
    browser.quit()
