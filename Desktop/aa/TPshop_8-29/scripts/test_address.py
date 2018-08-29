from base.base_driver import init_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        self.page.home.click_mine()
        # 判断是否登录  没有登录 登录
        if not self.page.mine.is_login():
            self.page.mine.click_login_sign_up()
            self.page.login.login()
        # 已经登录了  点击收货地址
        if self.page.mine.is_location_exist_scroll_page(self.page.mine.address_button):
            self.page.mine.click_address()
            self.page.address.click_new_address()
            self.page.new_address.input_name("xiaoming")
            self.page.new_address.input_mobile("13800138000")
            self.page.new_address.input_address("beijing")
            self.page.new_address.click_region()
            # 点击四次城市
            self.page.region.click_city()
            # 点击确定
            self.page.region.click_commit()
            # 点击保存收货地址
            self.page.new_address.click_save_address()
            # 断言
            assert self.page.address.is_toast_exist("添加成功")
        else:
            assert False

