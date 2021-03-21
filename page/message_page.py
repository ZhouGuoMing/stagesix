# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : message_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.addressbook_page import AddressbookPage
from page.base_page import BasePage


class MessagePage(BasePage):
    def goto_addressbook(self):
        self.parse_action("../page/message_page.yaml", "goto_addressbook")
        # self.find_click(MobileBy.XPATH, '//*[@text="通讯录"]')
        # self.find_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']")
        return AddressbookPage(self.driver)

