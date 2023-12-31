from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//button[contains(text(), "I want to go on a magical journey!")]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button1 = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()