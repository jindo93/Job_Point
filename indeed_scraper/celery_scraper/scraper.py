#!/usr/bin/env python3

from celery import Celery

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from schema import input_job_data
from indeed_page import IndeedPage
from auth import BROKER
import logger as Log

app = Celery('scraper', broker=BROKER)


def get_driver():
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1440, 900)
        # driver = webdriver.Chrome()
        return driver
    except:
        Log.log_message('FAILED TO GET DRIVER!')


def save_job_data(job_title, state, job_details):
    try:
        Log.job_data_to_csv(job_details, state)
        # input_job_data(job_details, state) FIXME
        Log.log_message("{state}, {num_jobs}, {job_title}  job data saved!".format(
            num_jobs=len(job_details), job_title=job_title, state=state))
    except:
        Log.log_message("ERROR SAVING DATA: " + state + ' ' + job_title)


@app.task
def scrape_jobs(job_title, state):
    Log.instantiate_csv(state)
    browser = get_driver()
    try:
        ip = IndeedPage(driver=browser)
        ip.go()
        ip.search_input.input_text(job_title)
        loc = ip.search_location_text
        loc.click()
        loc.manual_clear()
        loc.input_text(state)
        ip.search_job_button.click()

        job_details = []

        while ip.check_next_page:
            job_details.extend(ip.get_job_details(ip.get_job_cards))
            ip.next_page_button.click_next_page()
            if ip.check_popup:
                ip.popup.click()

            if len(job_details) > 1000:
                save_job_data(job_title, state, job_details)
                job_details = []
                # break  # TODO Comment out for production mode
        if len(job_details) > 0:
            save_job_data(job_title, state, job_details)
            job_details = []

        Log.log_message("COMPLETED JOB SCRAPING: " +
                        job_title + ' ' + state + '\n')
        browser.quit()
        return None
    except:
        Log.log_message("ERROR SCRAPING DATA: " +
                        state + ' ' + job_title + '\n')
        browser.quit()
        return None
