from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    time.sleep(1)
    
    #Считываем значение переменной Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    #Вставляем ответ в инпут
    input_num = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_num.send_keys(y)
    time.sleep(1)

    #Отметить checkbox "I'm the robot".
    label = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    label.click()
    time.sleep(1)

    #Выбрать radiobutton "Robots rule!".
    r_button = browser.find_element(By.CSS_SELECTOR, "input#robotsRule.form-check-input")
    r_button.click()
    time.sleep(1)

    #Нажать на кнопку Submit.
    sub_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    sub_button.click()

finally:
    time.sleep(10)
    browser.quit()
