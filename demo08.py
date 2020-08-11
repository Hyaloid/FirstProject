from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)

    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)  # 线程的阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.quit()

    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)  # 线程的阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.quit()

    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)
        # 若2s之后还没有加载出tab上面标题为'百度一下，你就知道'那么就抛出异常 否则就执行后续的代码
        wait.until(EC.title_is('百度一下，你就知道'))

        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)  # 线程的阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_wait()
