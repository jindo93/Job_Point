#!/usr/bin/env python3

from py2neo import Graph
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from schema import input_job_data
from indeed_page import IndeedPage
from utils.auth import NEO4J_USR, NEO4J_PW


graph = Graph("bolt://localhost:7687", auth=(NEO4J_USR, NEO4J_PW))

if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1440, 900)

    job_title = 'data scientist'

    indeed = IndeedPage(driver=browser)
    indeed.go()
    indeed.search_input.input_text(job_title)
    indeed.search_job_button.click()

    job_details = []

    while indeed.next_page_button:
        # cards = indeed.get_job_cards.delay().get()
        # job_details.extend(
        #     [group([indeed.get_job_title.s(e),
        #             indeed.get_job_post_url.s(e),
        #             indeed.get_company.s(e),
        #             indeed.get_location.s(e)] for e in cards)().get()]
        # )
        job_details.extend(indeed.get_job_details(indeed.get_job_cards))
        indeed.next_page_button.click_next_page()
        next_page = indeed.next_page_button

        try:
            indeed.popup.click()
        except:
            pass
        if len(job_details) > 100:
            input_job_data(graph, job_details)
            job_details = []
            break
    input_job_data(graph, job_details)
    job_details = []
    print('All jobs titled <' + job_title + '> have been scraped')
    browser.close()
