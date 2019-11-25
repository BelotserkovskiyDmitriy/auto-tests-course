from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(int_valueX):
    return str(math.log(abs(12*math.sin(int_valueX))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    magic_button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    time.sleep(1)
    magic_button.click()

    #Переход на вторую вкладку
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    web_valueX = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    int_valueX = int(web_valueX.text)
    answer = calc(int_valueX)

    fill_answer = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    fill_answer.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
    
