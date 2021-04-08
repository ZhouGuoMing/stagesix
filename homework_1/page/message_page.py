# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : message_page.py

from homework_1.page.addressbook_page import AddressbookPage
from homework_1.page.base_page import BasePage


class MessagePage(BasePage):
    def goto_addressbook(self):
        self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_1/page/message_page.yaml", "goto_addressbook")
        # self.find_click(MobileBy.XPATH, '//*[@text="通讯录"]')
        # self.find_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']")
        return AddressbookPage(self.driver)

