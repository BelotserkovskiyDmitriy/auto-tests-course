from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='firstname']")
    first_name.send_keys("Добрыня")

    last_name = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='lastname']")
    last_name.send_keys("Никитич")

    email = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='email']")
    email.send_keys("dobrinia1015@gmal.com")

    send_file = browser.find_element(By.CSS_SELECTOR, "input#file[type='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.odt')        # добавляем к этому пути имя файла 
    send_file.send_keys(file_path)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
