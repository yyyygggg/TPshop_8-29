from time import sleep

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    # 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    # 登录
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    # 显示密码按钮
    view_password = By.ID, "com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach("用户名是", text)
        self.input(self.username_edit_text, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach("密码是", text)
        self.input(self.password_edit_text, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)

    def login(self):
        self.input_username("15210048487")
        sleep(1)
        self.input_password("123456")
        sleep(1)
        self.click_login()

    @allure.step(title='判断登录按钮是否可用')
    def is_login_button_enabled(self):
        self.is_location_enabled(self.login_button)

    @allure.step(title='点击显示密码按钮')
    def click_view_password(self):
        self.click(self.view_password)