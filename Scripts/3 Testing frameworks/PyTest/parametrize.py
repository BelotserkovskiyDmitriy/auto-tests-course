import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope='function')
def browser():
    print("Starting browser...")
    browser = webdriver.Chrome()
    yield browser
    print("Quit browser.")
    browser.quit()

@pytest.mark.parametrize('page_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_input_answer(browser, page_number):
    link = f"https://stepik.org/lesson/{page_number}/step/1"
    browser.get(link)
    time.sleep(3)
    answer_field = browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']")
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))
    send_btn = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    send_btn.click()


    message = browser.find_element(By.CSS_SELECTOR, "pre.smart_hints.hint")
