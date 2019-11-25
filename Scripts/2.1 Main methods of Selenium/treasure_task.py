from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    #Считываем значение Х и решаем уравнение
    image = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    value_of_x = image.get_attribute("valuex")
    answer = calc(value_of_x)

    #Ввод ответа в инпут
    ans_input = browser.find_element(By.CSS_SELECTOR, "input#answer[type='text']")
    ans_input.send_keys(answer)

    #Отмечаем нужный чекбокс и радиобатн
    check_box = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox.check-input")
    check_box.click()

    radio_btn = browser.find_element(By.CSS_SELECTOR, "input#robotsRule.check-input")
    radio_btn.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
