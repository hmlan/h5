from page.base_page import PageBase
from selenium.webdriver.common.by import By
class IndexPage(PageBase):
    # 定位器

    mine_button_loc = By.XPATH, "//div[text()='我的']"

    def mine_button(self):
        self.wait(self.mine_button_loc)
        self.find_element(self.mine_button_loc).click()


