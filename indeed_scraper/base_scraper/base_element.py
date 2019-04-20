#!/usr/bin/env python3

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

cwd = os.getcwd()


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None

    def find_elem(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            self.web_element = element
            return None
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Element Not Found!: {locator} \n'.format(
                    locator=self.locator))
            f.close()

    def find_elems(self):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator=self.locator)
            )
            self.web_element = elements
            return None
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Elements Not Found!: {locator} \n'.format(
                    locator=self.locator))
            f.close()

    def find_next_page(self):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator=self.locator)
            )
            element = elements[-1]
            self.web_element = element
            return None
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Next Page Not Found!: {locator} \n'.format(
                    locator=self.locator))
            f.close()

    def input_text(self, txt):
        try:
            self.web_element.send_keys(txt)
            return None
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Unable to Send Input Text! \n')
            f.close()

    def click(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator=self.locator)
            )
            element.click()
            return None
        except:
            with open(cwd+'/log.txt') as f:
                f.write('Unable to Click!: {locator} \n'.format(
                    locator=self.locator))
            f.close()

    def click_next_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator=self.locator)
            )
            self.web_element.click()
            return None
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Next Page Not Clicked!: {locator} \n'.format(
                    locator=self.locator))
            f.close()

    def attribute(self, attr):
        try:
            attribute = self.web_element.get_attribute(attr)
            return attribute
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Attribute Not Found!: {attr} \n'.format(attr=attr))

    def manual_clear(self):
        for i in range(30):
            self.web_element.send_keys(Keys.BACK_SPACE)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def check_popup(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            if element:
                return True
        except:
            return False

    def check_next_page(self):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator=self.locator)
            )
            element = elements[-1]
            if element:
                return True
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('Next Page Not Found!: {locator} \n'.format(
                    locator=self.locator))
            f.close()
