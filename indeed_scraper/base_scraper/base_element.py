#!/usr/bin/env python3

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None

    def find_elem(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        #print('element: ', element)
        self.web_element = element
        return None

    def find_elems(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator=self.locator)
        )
        self.web_element = elements
        #print('elements: \n', elements)
        return None

    def find_next_page(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator=self.locator)
        )
        element = elements[-1]
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None

    def click_next_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        self.web_element.click()
        return None

    def attribute(self, attr):
        attribute = self.web_element.get_attribute(attr)
        return attribute

    def manual_clear(self):
        for i in range(30):
            self.web_element.send_keys(Keys.BACK_SPACE)
        # self.web_element.send_keys(Keys.CLEAR)
        # while self.web_element.text:
        #     self.web_element.send_keys(Keys.BACK_SPACE)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text
