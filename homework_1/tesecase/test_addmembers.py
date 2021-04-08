# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : tesrdemo.py
from homework_1.page.app import App



class TestDemo:
    def setup(self):
        self.app=App()
    def teardown(self):
        self.app.goto_message().driver.quit()


    def test_address(self):
        str_a="添加成功"
        goto_address_book= self.app.goto_message().goto_addressbook()
        goto_add_members= goto_address_book.goto_add_members()[1]
        goto_address_book.back_to_message()
        assert str_a == goto_add_members







