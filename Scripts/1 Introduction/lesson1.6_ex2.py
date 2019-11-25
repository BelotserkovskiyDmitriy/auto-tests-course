#Глава 1.6 Задание 2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
time.sleep(1)

#Выбираем нужный линк
link = browser.find_element(By.LINK_TEXT, '224592')
link.click()

#Заполняем форму
first_name = browser.find_element(By.CSS_SELECTOR, "input[name=\"first_name\"]")
first_name.send_keys("Афанасий")

last_name = browser.find_element(By.CSS_SELECTOR, "input[name=\"last_name\"]")
last_name.send_keys("Шмонько")

city = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
city.send_keys("Питсбург")

country = browser.find_element(By.CSS_SELECTOR, "#country")
country.send_keys("Великая Британия")

button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
time.sleep(1)
button.click()

time.sleep(10)
browser.quit()                              
