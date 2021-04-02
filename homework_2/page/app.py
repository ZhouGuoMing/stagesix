# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : app.py
from appium import webdriver
from homework_2.page.message_page import MessagePage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps={}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def goto_message(self):
        return MessagePage(self.driver)