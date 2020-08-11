from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # self.driver.get('http://sahitest.com/demo/clicks.htm')

    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()
        time.sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        time.sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()

    def test_keys(self):
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        kw.send_keys(Keys.COMMAND, 'a')
        time.sleep(2)
        kw.send_keys(Keys.COMMAND, 'x')
        time.sleep(2)
        kw.send_keys(Keys.COMMAND, 'v')
        self.driver.quit()

    def test_mouse_move(self):
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text('新闻')).perform()
        time.sleep(2)

if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    case.test_keys()
    # case.test_mouse_move()