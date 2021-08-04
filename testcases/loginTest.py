import unittest
import HTMLTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users/sachin/PycharmProjects/python_selenium")
import time
from pageobject.loginpage import locators

class login_test(unittest.TestCase):
    url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username=''
    password=''

    driver=webdriver.Chrome()
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
    def test_login(self):
        lp=locators(self.driver)
        lp.set_user_name(self.username)
        lp.set_password(self.password)
        lp.click_login()
        time.sleep(5)
        lp.click_logout()
        #self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"webpage title not match")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()