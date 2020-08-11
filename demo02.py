from selenium import webdriver
import time

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)  # 用于进行不同页面中不同tab之间的切换
        print(self.driver.page_source)
        time.sleep(3)
        self.driver.quit()  # 关闭浏览器
    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.forward()

        time.sleep(3)
        self.driver.close()  # 关闭当前tab
    def test_window(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                time.sleep(2)

if __name__ =="__main__":
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_window()

