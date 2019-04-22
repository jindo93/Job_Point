#!/usr/bin/env python3

from py2neo import Graph
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from schema import input_job_data
from indeed_page import IndeedPage
from auth import URL, NEO4J_USR, NEO4J_PW
import os

graph = Graph(URL, auth=(NEO4J_USR, NEO4J_PW))
cwd = os.getcwd()


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
        with open(cwd+"/log.txt", "a") as f:
            f.write('FAILED TO GET DRIVER! \n')
        f.close()


def scrape_jobs(job_title):
    browser = get_driver()
    try:
        ip = IndeedPage(driver=browser)
        ip.go()
        ip.search_input.input_text(job_title)
        loc = ip.search_location_text
        loc.click()
        loc.manual_clear()
        ip.search_job_button.click()

        job_details = []

        while ip.next_page_button:
            job_details.extend(ip.get_job_details(ip.get_job_cards))
            ip.next_page_button.click_next_page()
            if ip.check_popup:
                ip.popup.click()

            if len(job_details) > 50:
                with open(cwd+'/log.txt', 'a') as f:
                    f.write("{num_jobs} job details added for {job_title} \n".format(
                        num_jobs=len(job_details), job_title=job_title))
                f.close()
                input_job_data(graph, job_details)
                job_details = []
                break  # TODO Comment out for production mode
        if len(job_details) > 0:
            input_job_data(graph, job_details)
        job_details = []
        with open(cwd+'/log.txt', 'a') as f:
            f.write('All jobs titled <' + job_title + '> have been scraped \n')
        f.close()
        browser.quit()
        return True
    except:
        browser.quit()
        with open(cwd+'/log.txt', 'a') as f:
            f.write('ERROR SCRAPING {job_title}'.format(job_title=job_title))
        f.close()


if __name__ == '__main__':
    job_titles = ['software engineer', 'data engineer']
    for job in job_titles:
        scrape_jobs(job)
