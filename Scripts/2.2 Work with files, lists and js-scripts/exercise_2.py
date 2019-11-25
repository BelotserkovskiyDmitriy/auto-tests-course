from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#Магия
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

#Находим значение х и вычесляем ответ уравнения
#Почему вместо строки x_str = x_value.text нельзя написать x_str = str(x_value)?
x_value = browser.find_element(By.CSS_SELECTOR, "span#input_value")
x_str = x_value.text
x = int(x_str)
y = calc(x)

#Скролим
browser.execute_script("window.scrollBy(0,100);")

answer = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
answer.send_keys(y)

checkBox = browser.find_element(By.CSS_SELECTOR, "label.form-check-label")
checkBox.click()
time.sleep(1)

radioBut = browser.find_element(By.CSS_SELECTOR, "input#robotsRule.form-check-input")
radioBut.click()
time.sleep(1)

submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
submit_button.click()
time.sleep(10)

browser.qiut()






