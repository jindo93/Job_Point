from scraper import scrape_jobs

if __name__ == '__main__':
    job_title = 'computer, programming, tech, software, data, information'
    states = ["NY", "CA", "TX", "MA", "TN", "FL", "VA", "IL", "OR",
              "SC", "PA", "OH", "IN", "NC", "GA", "MD", "MI", "NJ",
              "CO", "AZ", "WA", "MN", "WI", "MO", "CT", "AL", "LA",
              "KY", "UT", "IA", "OK", "KS", "NV", "AR", "NE", "NM",
              "NH", "MS", "WV", "ID", "ME", "RI", "DE", "MT", "ND",
              "SD", "VT", "WY", "DC", "AK"]
    for state in states:
        scrape_jobs.delay(job_title, state)
