import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegionPage(BaseAction):

    city_text_view = By.ID, "com.tpshop.malls:id/tv_city"

    commit_button = By.ID, "com.tpshop.malls:id/btn_right"

    def click_city(self):
        for i in range(4):
            # 获取所有的 com.tpshop.malls:id/tv_city
            cities = self.find_elements(self.city_text_view)
            # 获取elements的长度  根据长度生成随机数
            city_index = random.randint(0, len(cities) - 1)
            # 在列表中随机获取一个元素进行点击
            cities[city_index].click()
            time.sleep(1)

    def click_commit(self):
        self.click(self.commit_button)
