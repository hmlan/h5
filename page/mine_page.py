from page.base_page import PageBase
from selenium.webdriver.common.by import By

class MinePage(PageBase):
    # 定位器
    login_button_loc = By.XPATH, "//div[text()='点击登录']"

    def login_button(self):
        self.wait(self.login_button_loc)
        self.find_element(self.login_button_loc).click()

    