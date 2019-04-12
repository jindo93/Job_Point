#!/usr/bin/env python3

import celery

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from namedtuples.locator import Locator
from utils.auth import BROKER, BACKEND

url = 'https://www.indeed.com'

app = celery.Celery('indeed_page1.py',
                    broker=BROKER,
                    backend=BACKEND)


def go(driver):
    driver.get(url)


def job_search(driver):
    locator = Locator(by=By.ID, value='text-input-what')
    element = get_element(driver, locator)
    return element


def input_text(element, txt):
    try:
        element.send_keys(txt)
        return None
    except:
        return False


def click_job_search_button(driver):
    locator = Locator(by=By.CLASS_NAME, value='icl-Button')
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator=locator)
    )
    element.click()
    return None


def next_page_button(driver):
    try:
        locator = Locator(by=By.LINK_TEXT, value="Next »")
        element = get_element(driver, locator)
        return element
    except:
        return False


def click_next_page_button(driver):
    locator = Locator(
        by=By.XPATH, value="//div[@class='pagination']/a"
    )
    elements = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator=locator)
    )
    element = elements[-1]
    element.click()
    return None


def click_popup(driver):
    locator = Locator(by=By.XPATH, value="//div[@id='popover-x']/a")
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator=locator)
    )
    element.click()
    return None


def get_element(driver, locator):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator=locator)
    )
    print('element: ', element)
    return element


def get_elements(driver, locator):
    elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(locator=locator)
    )
    return elements


def popup(driver):
    try:
        locator = Locator(by=By.XPATH, value="//div[@id='popover-x']/a")
        element = get_element(driver, locator)
        return element
    except:
        return False


@app.task
def get_job_cards(driver):
    locator = Locator(by=By.CLASS_NAME, value='jobsearch-SerpJobCard')
    elements = get_elements(driver, locator)
    return elements


@app.task
def get_job_title(web_element):
    job_title = web_element.find_element(By.CLASS_NAME, 'jobtitle').text
    return job_title


@app.task
def get_job_post_url(web_element):
    url = web_element.find_element(
        By.CLASS_NAME, 'jobtitle'
    ).get_attribute('href')

    if url == None:
        url = web_element.find_element(
            By.CLASS_NAME, 'turnstileLink'
        ).get_attribute('href')
    return url


@app.task
def get_company(web_element):
    try:
        company = web_element.find_element(By.CLASS_NAME, 'company').text
        return company
    except:
        company = "Unnamed"
        return company


@app.task
def get_location(web_element):
    location = web_element.find_element(By.CLASS_NAME, 'location').text
    return location


# def click(driver, locator):
#     element =WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable(locator)
#     )
#     element.click()
#     return None

# def get_job_details(web_elements):
#     job_details = [[get_job_title(e),
#                     get_job_post_url(e),
#                     get_company(e),
#                     get_location(e)] for e in web_elements]
#     return job_details
