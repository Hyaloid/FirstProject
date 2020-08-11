from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver.maximize_window()
# time.sleep(1)
#
# element = driver.find_element_by_id('kw')
# element.send_keys('selenium')
# print(type(element))
#
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.quit()

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        time.sleep(1)
    def test_id(self):
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        print(type(element))

        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        # self.driver.quit()
    def test_name(self):
        # 该方法可能返回多个元素
        # find_element_by_name() 返回第一个
        # find_elements_by_name() 返回一个集合
        name = self.driver.find_element_by_name('wd')
        name.send_keys('selenium')
        print(type(name))

        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.quit()
    def test_xpath(self):
        xpath = self.driver.find_element_by_xpath('//*[@id="kw"]')
        xpath.send_keys('element')

        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.quit()
    def test_linktext(self):
        self.test_id()
        text = self.driver.find_element_by_link_text('百度首页')
        text.click()

        time.sleep(3)
        self.driver.quit()
    def test_partial_link_test(self):
        self.test_id()
        partial_link_text = self.driver.find_element_by_partial_link_text('首页')
        partial_link_text.click()

        time.sleep(3)
        self.driver.quit()
    def test_tag(self):
        # 一般用得很少，很难根据tag定位，页面代码里面tag太多了
        input = self.driver.find_element_by_tag_name('input')
        print(input)
    def test_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

        time.sleep(3)
        self.driver.quit()
    def test_class_name(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

        time.sleep(3)
        self.driver.quit()
    def test_all(self):
        # 默认通过id来定位
        self.driver.find_element(By.ID, value='kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    case = TestCase()
    # case.test_id()
    # case.test_name()
    # case.test_xpath()
    # case.test_linktext()
    # case.test_partial_link_test()
    # case.test_tag()
    # case.test_css_selector()
    # case.test_class_name()
    # case.test_all()