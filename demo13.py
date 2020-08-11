from selenium import webdriver
import time

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://sahitest.com/demo/framesTest.htm')
    def test1(self):
        top = self.driver.find_element_by_name('top')
        self.driver.switch_to.frame(top)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()

        time.sleep(3)
        self.driver.switch_to.default_content()
        second = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(second)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()

if __name__ == '__main__':
    case = TestCase()
    case.test1()
    case.driver.quit()
