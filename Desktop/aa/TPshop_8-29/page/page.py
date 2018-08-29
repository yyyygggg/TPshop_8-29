from page.address_page import AddressPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.new_address_page import NewAddressPage
from page.region_page import RegionPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def address(self):
        return AddressPage(self.driver)

    @property
    def new_address(self):
        return NewAddressPage(self.driver)

    @property
    def region(self):
        return RegionPage(self.driver)