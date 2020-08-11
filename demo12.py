from selenium import webdriver
import time
import os



class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com/')

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

        time.sleep(2)
        # 保存到当前项目的路径下
        # self.driver.save_screenshot('baidu.png')
        st = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        file_name = st + '.png'
        # self.driver.save_screenshot(file_name)
        path = os.path.abspath('screenshot')
        if not os.path.exists(path):
            os.mkdir(path)
        file_path = path + '/' + file_name
        self.driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    case = TestCase()
    case.test1()