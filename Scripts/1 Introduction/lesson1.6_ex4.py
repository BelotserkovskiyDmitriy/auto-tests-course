from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #пример xpath
    # //div[@class="row"]/div[2]

    first_name = browser.find_element(By.CSS_SELECTOR, "input[name=\"first_name\"]")
    first_name.send_keys("Афанасий")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[name=\"last_name\"]")
    last_name.send_keys("Шмонько")

    city = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    city.send_keys("Питсбург")
    
    country = browser.find_element(By.CSS_SELECTOR, "#country")
    country.send_keys("Великая Британия")

    sub_button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()
    
