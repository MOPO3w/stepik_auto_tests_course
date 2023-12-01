from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import unittest

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("example@example.com")    
        button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text        
        time.sleep(5)
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Wrong text")
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("example@example.com")    
        button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text        
        time.sleep(5)
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Wrong text")
if __name__ == "__main__":
    unittest.main()