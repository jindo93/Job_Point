from scraper import scrape_jobs

if __name__ == '__main__':
    job_title = 'computer, programming, tech, software, data, information'
    states = ["NY", "CA", "TX", "MA"]
    for state in states:
        scrape_jobs.delay(job_title, state)
