from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_element(driver, *args):
    e = driver.find_element(*args)
    return e

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    # get_element(driver, By.ID, 'kw').send_keys('selenium')
    # get_element(driver, By.ID, 'su').click()

    loc = (By.ID, 'kw')
    loc2 = (By.ID, 'su')
    get_element(driver, *loc).send_keys('selenium')
    time.sleep(2)
    get_element(driver, *loc2).click()
    time.sleep(2)
    driver.quit()