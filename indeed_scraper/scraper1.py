#!/usr/bin/env python3

from py2neo import Graph
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import celery
from celery import group

from schema import input_job_data
import indeed_page1 as ip

graph = Graph("bolt://localhost:7687", auth=(NEO4J_USR, NEO4J_PW))

if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1440, 900)

    job_title = 'data scientist'

    ip.go(driver)
    ip.input_text(ip.job_search(driver), job_title)
    ip.click_job_search_button(driver)

    job_details = []

    while ip.next_page_button(driver):
        job_cards = ip.get_job_cards.delay(driver).get()

        job_details.extend(
            [group(
                [ip.get_job_title.s(e),
                 ip.get_job_post_url.s(e),
                 ip.get_company.s(e),
                 ip.get_location.s(e)] for e in job_cards)().get()]
        )

        ip.click_next_page_button(driver)

        if ip.popup(driver):
            ip.click_popup(driver)

        if len(job_details) > 100:
            input_job_data(graph, job_details)
            job_details = []
            break
    input_job_data(graph, job_details)
    job_details = []
    print('All jobs titled <' + job_title + '> have been scraped')
    driver.close()
