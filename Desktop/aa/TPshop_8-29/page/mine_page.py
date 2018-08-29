from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MinePage(BaseAction):
    # 登录注册按钮
    login_sign_up_button = By.XPATH, "//*[@text='登录/注册']"
    # 设置按钮
    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"
    # 判断是否登录按钮
    is_login_button = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"
    # 收获地址按按钮
    address_button = By.XPATH, "//*[@text='收货地址']"

    def click_login_sign_up(self):
        self.click(self.login_sign_up_button)

    def click_setting(self):
        self.click(self.setting_button)

    def is_login(self):
        self.click_setting()
        is_login = not self.find_element(self.is_login_button).text == '登录'
        self.press_back()
        return is_login

    def click_address(self):
        self.click(self.address_button)
