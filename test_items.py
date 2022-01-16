import time
from selenium.webdriver.common.by import By


def test_button_language_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    buy_button = browser.find_element(By.CSS_SELECTOR,"[class = 'btn btn-lg btn-primary btn-add-to-basket']")
    assert buy_button, "Кнопку украли"


