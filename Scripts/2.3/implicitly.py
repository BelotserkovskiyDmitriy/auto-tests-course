from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element(By.ID, "button")

finally:
    browser.quit()
