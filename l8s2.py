from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "num1")
    input2 = browser.find_element(By.ID, "num2")
    x=int(input1.text)+int(input2.text)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(f'{x}')
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
