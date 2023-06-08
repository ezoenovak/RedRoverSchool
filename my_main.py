from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import string
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.select import Select


def test_waits_book():
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    driver.find_element(By.ID, "book").click()
    num = driver.find_element(By.ID, "input_value")
    x = int(num.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.ID, "solve").click()
    time.sleep(15)
    driver.quit()

def test_accept_alert():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    # confirm = browser.switch_to.alert
    # confirm.accept()
    browser.switch_to.alert.accept()
    num = browser.find_element(By.ID, "input_value")
    x = int(num.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)
    browser.quit()