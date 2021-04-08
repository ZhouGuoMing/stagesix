# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : addressbook_page.py
from homework_1.page.base_page import BasePage




class AddressbookPage(BasePage):


    def goto_add_members(self):
        str1= self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_1/page/addressbook_page.yaml", "goto_add_members")
        # self.swip_click("添加成员")
        # self.find_click(MobileBy.XPATH, '//*[@text="手动输入添加"]')
        # self.find(MobileBy.XPATH,'//android.widget.TextView[@text="姓名　"]'
        #                          '/following-sibling::android.widget.EditText').send_keys(name)
        # self.find(MobileBy.XPATH, '//android.widget.TextView[@text="手机　"]/../android.widget.RelativeLayout/'
        #                           'android.widget.RelativeLayout/android.widget.EditText').send_keys(phone)
        # self.find_click(MobileBy.XPATH, '//*[@text="保存"]')
        # str1 = self.find(MobileBy.XPATH, '//android.widget.Toast').text
        print(str1)
        return self.driver, str1

    def back_to_message(self):
        self.parse_action("D:/PycharmProjects/pythonProject/stagesix/homework_1/page/addressbook_page.yaml", "back_to_message")
        # self.find_click(MobileBy.ID, "com.tencent.wework:id/ig0")
















