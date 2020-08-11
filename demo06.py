from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms3.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element_by_id('provise')
        select = Select(se)

        # select.select_by_index(2)
        #
        # time.sleep(2)
        #
        # select.select_by_value('bj')
        # time.sleep(2)
        # select.select_by_visible_text('Tianjin')
        # time.sleep(2)
        # for i in range(3):
        #     select.select_by_index(i)
        #     time.sleep(2)
        # select.deselect_all()
        # time.sleep(3)
        # self.driver.quit()

        for option in select.options:
            print(option.text)
        self.driver.quit()


if __name__ == "__main__":
    case = TestCase()
    case.test_select()
