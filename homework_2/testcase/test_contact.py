# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : test_contact.py
from homework_2.page.app import App

class TestContact:
    def setup(self):
        self.app=App()
    def teardown(self):
        self.app.goto_message().driver.quit()

    def test_delete_contact(self):
        elements=self.app.goto_message().goto_addressbook().goto_search()
        elements_1 = elements.search()[1]
        len1=len(elements_1)
        elements_2 = elements.search_to_delete()[1]
        len2=len(elements_2)
        assert len1 >len2
