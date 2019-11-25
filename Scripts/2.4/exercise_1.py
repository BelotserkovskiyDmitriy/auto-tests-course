from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    wait_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    book_button = browser.find_element(By.CSS_SELECTOR, "button#book.btn.btn-primary")
    book_button.click()

    def calculate(int_valueX):
        return str(math.log(abs(12*math.sin(int_valueX))))

    web_valueX = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    int_valueX = int(web_valueX.text)
    answer = calculate(int_valueX)

    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_field.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button#solve.btn.btn-primary")
    submit_button.click()
    
finally:
    time.sleep(5)
    browser.quit()
