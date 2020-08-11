from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

# http://sahitest.com/demo/


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.driver.maximize_window()
    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        e1 = WebElement
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)
        self.driver.quit()
    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        print(e.value_of_css_property('font'))

        time.sleep(2)
        e.clear()
        self.driver.quit()
    def test_method2(self):
        form_element = self.driver.find_element_by_xpath('/html/body/form[1]')
        form_element.find_element_by_id('t1').send_keys('hello world')



if __name__ == "__main__":
    case = TestCase()
    # case.test_webelement_prop()
    # case.test_webelement_method()
    case.test_method2()