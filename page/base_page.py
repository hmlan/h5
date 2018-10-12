from selenium.webdriver.support.wait import WebDriverWait

class  PageBase():
    def __init__(self,driver):
        self._driver=driver

    def open(self,url):
        self._driver.get(url)

    def find_element(self,locator):
        return self._driver.find_element(*locator)

    def wait(self,locator, time_out=10):
        wait_ = WebDriverWait(self._driver,time_out)
        wait_.until(lambda driver: driver.find_element(*locator))

    def switch(self,text):
        self._driver.switch_to.frame(text)

