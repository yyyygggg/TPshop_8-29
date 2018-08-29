import random
from time import sleep

import allure
import pytest
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def show_password_random():
    temp_list = list()
    for i in range(2):
        temp_list.append(random_password())
    return temp_list


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize('args', analyze_with_file("login_data", "test_login"))
    def test_login(self, args):
        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_username(args["username"])
        self.page.login.input_password(args["password"])
        self.page.login.click_login()
        assert self.page.login.is_toast_exist(args["expect"])

    @pytest.mark.parametrize('args', analyze_with_file("login_data", "test_login_miss"))
    def test_login_miss(self, args):
        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_username(args["username"])
        # sleep(2)
        self.page.login.input_password(args["password"])
        sleep(3)
        assert not self.page.login.is_login_button_enabled()

    @pytest.mark.parametrize('password', show_password_random())
    def test_show_password(self, password):
        # password = "111111"
        password_location = (By.XPATH, "//*[@text='%s']" % password)
        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_password(password)

        # if self.page.login.is_location_exist(password_location):
        #     assert False
        # 断言为真 继续运行 断言为假 结束运行
        assert not self.page.login.is_location_exist(password_location)
        # 点击显示密码按钮
        self.page.login.click_view_password()
        sleep(2)
        # 向报告里添加截图
        allure.attach("显示密码： ", self.driver.get_screenshot_as_png(), AttachmentType.PNG)

        assert self.page.login.is_location_exist(password_location)
