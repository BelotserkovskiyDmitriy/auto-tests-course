from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    #Находим числа,тайпкастим в инт,потом сумму назад в строку для поиска
    num1 = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
    num2 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap")

    str_num1 = num1.text
    str_num2 = num2.text
    
    summa = int(str_num1)+int(str_num2)
    str_summa = str(summa)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown.custom-select"))
    select.select_by_visible_text(str_summa)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
