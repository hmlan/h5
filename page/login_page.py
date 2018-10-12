from page.base_page import PageBase
from selenium.webdriver.common.by import By

class LoginPage(PageBase):
    # 定位器
    tel_input_loc = By.XPATH, "//input[@type='tel']"        # 手机号输入框
    pwd_input_loc = By.XPATH, "//input[@type='password']"   # 密码输入框
    submit_button_loc= By.CSS_SELECTOR, ".shj-box-padding.flex-row.justify-content-center.shj-btn"  #登录按钮

    def tel_input(self,text):
        self.wait(self.tel_input_loc)
        self.find_element(self.tel_input_loc).send_keys(text)

    def pwd_input(self,text):
        self.wait(self.pwd_input_loc)
        self.find_element(self.pwd_input_loc).send_keys(text)

    def submit_button(self):
        self.wait(self.submit_button_loc)
        self.find_element(self.submit_button_loc).click()