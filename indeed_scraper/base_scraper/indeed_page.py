#!/usr/bin/env python3

from celery import Celery

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_element import BaseElement
from base_page import BasePage
from namedtuples.locator import Locator
from namedtuples.job_post import JobPost
from utils.auth import BROKER, BACKEND

app = Celery('indeed_page',
             broker=BROKER,
             backend=BACKEND)


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
        try:
            locator = Locator(
                by=By.XPATH, value="//div[@class='pagination']/a"
            )
            element = BaseElement(
                self.driver, locator
            )
            element.find_next_page()
            return element
        except:
            print("next page not found")
            return False

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
                        self.get_location(e)] for e in web_elements]
        return job_details

    # @app.task
    def get_job_title(self, web_element):
        job_title = web_element.find_element(By.CLASS_NAME, 'jobtitle').text
        return job_title

    # @app.task
    def get_job_post_url(self, web_element):
        url = web_element.find_element(
            By.CLASS_NAME, 'jobtitle').get_attribute('href')
        if url == None:
            url = web_element.find_element(
                By.CLASS_NAME, 'turnstileLink').get_attribute('href')
        return url

    # @app.task
    def get_company(self, web_element):
        try:
            company = web_element.find_element(By.CLASS_NAME, 'company').text
            return company
        except:
            company = "Unnamed"
            return company

    # @app.task
    def get_location(self, web_element):
        location = web_element.find_element(By.CLASS_NAME, 'location').text
        return location


##### Celery Task Methods #####
    @app.task
    def get_job_cards1(self):
        locator = Locator(by=By.CLASS_NAME, value='jobsearch-SerpJobCard')
        elements = BaseElement(
            self.driver, locator
        )
        elements.find_elems()
        return elements.web_element

    @app.task
    def get_job_title1(self, web_element):
        job_title = web_element.find_element(By.CLASS_NAME, 'jobtitle').text
        return job_title

    @app.task
    def get_job_post_url1(self, web_element):
        url = web_element.find_element(
            By.CLASS_NAME, 'jobtitle').get_attribute('href')
        if url == None:
            url = web_element.find_element(
                By.CLASS_NAME, 'turnstileLink').get_attribute('href')
        return url

    @app.task
    def get_company1(self, web_element):
        try:
            company = web_element.find_element(By.CLASS_NAME, 'company').text
            return company
        except:
            company = "Unnamed"
            return company

    @app.task
    def get_location1(self, web_element):
        location = web_element.find_element(By.CLASS_NAME, 'location').text
        return location
