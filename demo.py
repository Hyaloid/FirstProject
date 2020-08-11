from selenium import webdriver
import time

def test2():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')

    time.sleep(1)
    driver.find_element_by_id('kw').send_keys('selenium')
    time.sleep(2)
    driver.find_element_by_id('su').click()

    time.sleep(1)
    driver.quit()


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://www.baidu.com/')

        time.sleep(1)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()

        time.sleep(1)
        self.driver.quit()


# def test():
#     import subprocess
#     p = subprocess.Popen('chromedriver')
#     p.communicate()


if __name__ == '__main__':
    # test()
    case = TestCase()
    case.test()