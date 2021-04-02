# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : base_page.py
import yaml
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self,loctor, value):
        return self.driver.find_element(loctor, value)

    def finds(self,loctor, value):
        return self.driver.find_elements(loctor, value)

    def find_click(self,loctor, value):
        return self.find(loctor,value).click()


    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def staleness_of(self,loctor, value):
        try:
            WebDriverWait(self.driver, 15).until(
            expected_conditions.staleness_of((loctor, value)))
            return True
        except TimeoutError:
            return False


    def parse_action(self,path,fun_name):
        with open(path,"r",encoding="utf-8") as f:
            function=yaml.safe_load(f)
            # print(function)
            steps:list[dict]=function[fun_name]
            # print(steps)
        for step in steps:
            if step["action"]=="find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"]=="find":
                if step["find_to_do"]=="text":
                    return self.find(step["by"], step["locator"]).text
                else:
                    self.find(step["by"], step["locator"])
            elif step["action"]== "finds":
                if step["finds_to_do"]=="return":
                    return self.finds(step["by"], step["locator"])
                else:self.finds(step["by"], step["locator"])
            elif step["action"]== "swip_click":
                self.swip_click(step["text"])
            elif step["action"]== "send_keys":
                self.find(step["by"], step["locator"]).send_keys(step["key"])
            elif step["action"]== "staleness_of":
                self.staleness_of(step["by"],step["locator"])
            elif step["action"]== "sleep":
                sleep(step["time"])


