# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : base_page.py
import json
import allure
import logging
import yaml
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)%(filename)s[line:%(lineno)d]%(levelname)s%(message)s',
                    # 打印日志的时间
                    datefmt='%a,%d%b%Y%H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    # 打开日志文件的方式
                    filemode='w'
                   )

class BasePage:

    _params = {}
    _blacklist = [(MobileBy.ID, "com.tencent.wework:id/ig0"), (MobileBy.XPATH, '//*[@text="关闭"]')]
    _max_mun = 3
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def setup_implicitly_wait(self,timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, locator, value):
        logging.info(f"find: locator={locator}, value={value}")
        try:
            element=self.driver.find_element(locator, value)
            self._error_num=0
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            #处理黑名单
            self.setup_implicitly_wait(5)
            self.driver.get_screenshot_as_file("tem.png")
            allure.attach.file("tem.png", attachment_type=allure.attachment_type.PNG)
            #设置最大查找次数
            if self._error_num > self._max_mun:
                self._error_num=0
                self.setup_implicitly_wait(10)
                raise e
            # 每次进except一次都执行+1操作
            self._error_num +=1
            for ele in self._blacklist:
                eles=self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    self.setup_implicitly_wait(10)
                    return self.find(locator,value)
            raise e

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

    def staleness_of(self, loctor, value):
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
            # json.dumps()序列化 python对象转化成字符串
            # json.loads()反序列化 python字符串转化为python对象
            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace("${"+key+"}", value)
            steps = json.loads(raw)

        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                if step["find_to_do"] == "text":
                    return self.find(step["by"], step["locator"]).text
                else:
                    self.find(step["by"], step["locator"])
            elif step["action"] == "finds":
                if step["finds_to_do"]=="return":
                    return self.finds(step["by"], step["locator"])
                else:self.finds(step["by"], step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "send_keys":
                self.find(step["by"], step["locator"]).send_keys(step["text"])
            elif step["action"] == "staleness_of":
                self.staleness_of(step["by"], step["locator"])
            elif step["action"] == "sleep":
                sleep(step["time"])


