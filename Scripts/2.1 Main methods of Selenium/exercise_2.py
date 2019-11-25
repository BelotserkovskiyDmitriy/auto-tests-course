from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    people_radio = browser.find_element(By.ID, "peopleRule")

    #Найдем атрибут checked и его значение
    people_checked = people_radio.get_attribute("checked")
    print("Значение переменной people_radio: ", people_checked)
    assert people_checked is not None, "Эта кнопка не выбрана по умолчанию!"
finally:
    browser.quit()
