#!/usr/bin/env python3

import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_element import BaseElement
from base_page import BasePage
from locator import Locator

cwd = os.getcwd()


class IndeedPage(BasePage):
    url = 'https://indeed.com'

    @property
    def search_input(self):
        locator = Locator(by=By.ID, value='text-input-what')
        element = BaseElement(
            driver=self.driver,
            locator=locator
        )
        element.find_elem()
        return element

    @property
    def search_location_text(self):
        locator = Locator(by=By.ID, value='text-input-where')
        element = BaseElement(
            driver=self.driver,
            locator=locator
        )
        element.find_elem()
        return element

    @property
    def search_job_button(self):
        locator = Locator(by=By.CLASS_NAME, value='icl-Button')
        element = BaseElement(
            driver=self.driver,
            locator=locator
        )
        element.find_elem()
        return element

    @property
    def next_page_button(self):
        locator = Locator(
            by=By.XPATH, value="//div[@class='pagination']/a"
        )
        element = BaseElement(
            self.driver, locator
        )
        element.find_next_page()
        return element

    @property
    def popup(self):
        locator = Locator(
            by=By.XPATH, value="//div[@id='popover-x']/a")
        element = BaseElement(self.driver, locator)
        element.find_elem()
        return element

    # @app.task
    @property
    def get_job_cards(self):
        locator = Locator(by=By.CLASS_NAME, value='jobsearch-SerpJobCard')
        elements = BaseElement(
            self.driver, locator
        )
        elements.find_elems()
        return elements.web_element  # returns a list of job card web elements

    def get_job_details(self, web_elements):
        job_details = [[self.get_job_title(e),
                        self.get_job_post_url(e),
                        self.get_company(e),
                        self.get_location(e),
                        self.get_summary(e)] for e in web_elements]
        return job_details

    def get_job_title(self, web_element):
        try:
            job_title = web_element.find_element(
                By.CLASS_NAME, 'jobtitle').text
            return job_title
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('No job title!')
            f.close()

    def get_job_post_url(self, web_element):
        try:
            url = web_element.find_element(
                By.CLASS_NAME, 'jobtitle').get_attribute('href')
            if url == None:
                url = web_element.find_element(
                    By.CLASS_NAME, 'turnstileLink').get_attribute('href')
            return url
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('No post url..')
            f.close()

    def get_company(self, web_element):
        try:
            company = web_element.find_element(By.CLASS_NAME, 'company').text
            return company
        except:
            company = "Unnamed"
            with open(cwd+'/log.txt', 'a') as f:
                f.write('No company name..')
            f.close()
            return company

    def get_location(self, web_element):
        try:
            location = web_element.find_element(By.CLASS_NAME, 'location').text
            return location
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('No location..')
            f.close()

    def get_summary(self, web_element):
        try:
            summary = web_element.find_element(By.CLASS_NAME, 'summary').text
            return summary
        except:
            with open(cwd+'/log.txt', 'a') as f:
                f.write('No summary..')
            f.close()
