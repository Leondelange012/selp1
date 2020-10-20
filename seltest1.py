from selenium import webdriver
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def SetUpClass(cls):
        cls.driver = webdriver.Chrome(r'Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_name('q').send_keys('Automation step by step')
        self.driver.find_element_by_name('btnK').click()

    def test_search_Leon(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_name('q').send_keys('Leon De Lange')
        self.driver.find_element_by_name('btnK').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')









