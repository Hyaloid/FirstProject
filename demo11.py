from selenium import webdriver
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test1(self):
        self.driver.execute_script("alert('test')")
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)


if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    # case.test3()
    case.test4()
    time.sleep(3)
    case.driver.quit()
