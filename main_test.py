from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def find_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)

def find_id(id):
    return driver.find_element(By.ID, id)

driver = webdriver.Chrome()

driver.get('https://demoqa.com/')
driver.implicitly_wait(10)


button_elements = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div')
button_elements.click()

button_dynamic = driver.find_element(By.XPATH, '//*[@id="item-8"]/span')
button_dynamic.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="visibleAfter"]'))
)


text_box = find_xpath('//*[@id="item-0"]')
text_box.click()

find_id('userName').send_keys(Keys.NUMPAD1, Keys.NUMPAD2)


time.sleep(3)

