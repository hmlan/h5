import unittest
from selenium import webdriver
from page.index_page import IndexPage
from page.mine_page import MinePage
from page.login_page import LoginPage
from time import sleep

class TestOrder(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome()
    def test_shopping_success(self):
         tel = '13981401921'
         password = '123456'
         indexPage=IndexPage(self.driver)
         indexPage.open("http://172.18.0.50:9003/")
         sleep(3)
         indexPage.mine_button()#点击我的
         minePage=MinePage(self.driver)
         minePage.login_button()
         loginPage=LoginPage(self.driver)
         loginPage.tel_input(tel)
         loginPage.pwd_input(password)
         loginPage.submit_button()
         sleep(3)
    def tearDown(self):
       self.driver.quit()
