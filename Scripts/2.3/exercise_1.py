from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calculate(int_valueX):
    return str(math.log(abs(12*math.sin(int(int_valueX)))))
    
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    journey_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    journey_btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    web_valueX = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    int_valueX = int(web_valueX.text)
    answer = calculate(int_valueX)
    answer_input = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    answer_input.send_keys(answer)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
