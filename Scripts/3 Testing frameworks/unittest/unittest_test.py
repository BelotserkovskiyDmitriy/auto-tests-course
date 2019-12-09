import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Василий")

        second_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        second_name.send_keys("Петров")

        e_mail = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        e_mail.send_keys("petrov_vasia123@gmail.com")

        sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default") 
        time.sleep(3)
        sub_button.click()

        welcome_txt_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_txt_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Failure registration on first page!")
        
    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.htm"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Василий")

        second_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        second_name.send_keys("Петров")

        e_mail = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        e_mail.send_keys("petrov_vasia123@gmail.com")

        sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default") 
        
        sub_button.click()

        welcome_txt_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_txt_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Failure registration on second page!")

if __name__ == "__main__":
    unittest.main()

    
