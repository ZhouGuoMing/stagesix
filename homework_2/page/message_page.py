# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : message_page.py

from homework_2.page.base_page import BasePage
from homework_2.page.addressbook_page import AddressbookPage

class MessagePage(BasePage):
    def goto_schedule(self):
        self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_2/page/message_page.yaml", "goto_schedule")
        return self.driver

    def goto_daiban(self):
        self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_2/page/message_page.yaml", "goto_daiban")
        return self.driver

    def goto_addressbook(self):
        self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_2/page/message_page.yaml", "goto_addressbook")
        return AddressbookPage(self.driver)

