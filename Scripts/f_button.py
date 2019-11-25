from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("submit_button")
    button.click()

finally:
    browser.quit()
