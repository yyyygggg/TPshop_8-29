from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10.0, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(location_by, location_value))

    def find_elements(self, location, timeout=10.0, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(location_by, location_value))

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def press_key_code(self, keycode):
        cap_dict = self.driver.capabilities
        if cap_dict.get("automationName") == "Uiautomator2":
            self.driver.press_keycode(keycode)
        else:
            self.driver.keyevent(keycode)

    def press_back(self):
        self.press_key_code(4)

    def press_enter(self):
        self.driver.press_key_code(66)

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = self.find_element((By.XPATH, message), timeout, poll=0.1)
        return element.text

    def is_toast_exist(self, message):
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    def is_location_enabled(self, location):
        return self.find_element(location).get_attribute("enabled") == "true"

    def is_location_exist(self, location):
        try:
            self.find_element(location)
            return True
        except:
            return False

    def scroll_page_one_time(self, diretion='up'):
        screen_width = self.driver.get_window_size()['width']
        screen_height = self.driver.get_window_size()['height']
        center_width = screen_width * 0.5
        center_height = screen_height * 0.5
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0

        if diretion in ["up", "down"]:
            start_x = center_width
            start_y = screen_height * 0.75
            end_x = center_width
            end_y = screen_height * 0.25
        elif diretion in ["left", "right"]:
            start_x = screen_width * 0.75
            start_y = center_height
            end_x = screen_width * 0.25
            end_y = center_height

        if diretion in ["up", "left"]:
            self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
        elif diretion in ["down", "right"]:
            self.driver.swipe(end_x, end_y, start_x, start_y, 2000)
        else:
            raise Exception("diretion只能传入up/down/left/right")

        sleep(1)

    def is_location_exist_scroll_page(self, location):
        old_page_source = None
        new_page_source = self.driver.page_source
        while True:
            if self.is_location_exist(location):
                return True
            else:
                if not old_page_source == new_page_source:
                    self.scroll_page_one_time()
                    old_page_source = new_page_source
                    new_page_source = self.driver.page_source
                else:
                    return False
