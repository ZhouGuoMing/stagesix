# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : search_page.py
from appium.webdriver.common.mobileby import MobileBy

from homework_2.page.base_page import BasePage
class Search_Page(BasePage):

    def search(self):
        a=self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_2/page/search_page.yaml", "search")
        return self.driver, a

    def search_to_delete(self):
        a=self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_2/page/search_page.yaml", "search_to_delete")
        return self.driver, a

