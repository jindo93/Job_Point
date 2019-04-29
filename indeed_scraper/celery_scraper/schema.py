#!/usr/bin/env python3

from neo4j import GraphDatabase
import requests
import json
import os
import csv
import logger as Log

from auth import URL, NEO4J_USR, NEO4J_PW

driver = GraphDatabase.driver(URL, auth=(NEO4J_USR, NEO4J_PW))

cwd = os.getcwd()

def csv_to_database(file_name):
    try:
        with open('datafile/{file_name}'.format(file_name=file_name), 'r', newline='') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            with driver.session() as session:
                for row in reader:
                    try:
                        session.run(
                            "MERGE (j:Job {name: {j_name}, summary: {j_summary}, post_url: {url}})"
                            "MERGE (c:Company {name: {c_name}})"
                            "MERGE (l:Location {name: {l_name}})"
                            "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)",
                            j_name=row[0], j_summary=row[4], url=row[1],
                            c_name=row[2], l_name=row[3]
                        )
                    except:
                        Log.log_message("Error importing: ", row)
                session.close()
            f.close()
        print("Succeeded importing: ", file_name)
        return None
    except:
        print("Error importing: ", file_name)
        return None



def import_data():
    files = os.listdir("datafile")
    for file in files:
        if file.endswith(".csv"):
            try:
                csv_to_database(file)
            except:
                print("Error in File Import for: ", file)
    return None

def get_location_no_zip(state):
    collector = []
    with driver.session() as session:
        result = session.run("MATCH (l:Location) "
                             "WHERE l.name contains({state}) AND not l.name contains('1')"
                             "RETURN l.name", state=state)

        for record in result.records():
            collector.append({"location": record['l.name']})
        return collector


def get_zip_code(city, state):
    url = "https://www.zipcodeapi.com/rest/5ne7BC5xRHrVQTNIeGZutmklhWvs0q8fB3jELED2cdhHo2bqWAXjTVRaCRm7mZlE/city-zips.json/"
    res = json.loads(
        requests.get(url + city + '/' + state).text
    )
    if res:
        return res['zip_codes'][0]
    else:
        return None


def merge_zip_neo(location, zip_code):
    print(zip_code)
    with driver.session() as session:
        session.run(
            "MERGE (l:Location { name: {location}, zip_code: {zip_code} })", location=location, zip_code=zip_code)
    return None


def get_location_with_zip(state):
    collector = []
    with driver.session() as session:
        result = session.run("MATCH (l:Location)<-[:LOCATED]-(c:Company)-[:HAS]->(j:Job) "
                             "WHERE l.name contains({state}) AND l.name contains('1')"
                             "RETURN l.name, c.name, j.name, j.post_url", state=state)

        for record in result.records():
            collector.append({"location": record['l.name'], "company": record['c.name'],
                              "title": record['j.name'], "url": record['j.post_url']})
        return collector


def merge_zip1():
    data = get_location_with_zip("NY")
    for d in data:
        zips = [int(s) for s in d['location'].split() if s.isdigit()]
        d['zip_code'] = zips[0]
    return data


def merge_zip(state):
    locations = get_location_no_zip(state)
    for l in locations:
        s = l['location'].split(',')
        zip_code = get_zip_code(s[0].strip(), s[1].strip())
        print("location: ", l['location'], " zip code: ", zip_code)


def input_source():
    try:
        with driver.session() as session:
            session.run("CREATE (s:Source {name: 'Indeed'})")
        return True
    except:
        return False


def input_job_detail(job_detail, state):
    with driver.session() as session:
        session.run("MATCH (s:Source) WHERE s.name = 'Indeed'"
                    "MERGE (j:Job {name: {j_name}, summary: {summary}, post_url: {p_url}})"
                    "MERGE (c:Company {name: {c_name}})"
                    "MERGE (l:Location {name: {l_name}, state: {state}})"
                    "MERGE (s)<-[:FROM]-(j)"
                    "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)",
                    j_name=job_detail[0], summary=job_detail[4], p_url=job_detail[1],
                    c_name=job_detail[2], l_name=job_detail[3], state=state)
    return None


def input_job_data(job_details, state):
    try:
        with driver.session() as session:
            for job_detail in job_details:
                job_detail.append(state)
                session.run("MATCH (s:Source) WHERE s.name = 'Indeed'"
                            "MERGE (j:Job {name: {j_name}, summary: {summary}, post_url: {p_url}})"
                            "MERGE (c:Company {name: {c_name}})"
                            "MERGE (l:Location {name: {l_name}, state: {state}})"
                            "MERGE (s)<-[:FROM]-(j)"
                            "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)",
                            j_name=job_detail[0], summary=job_detail[4], p_url=job_detail[1],
                            c_name=job_detail[2], l_name=job_detail[3], state=job_detail[5])
        session.close()
        return None
    except:
        Log.log_message("FAILED TO INPUT DATA: " + state)

# def input_job_data(job_details, state):
#     try:
#         for job_detail in job_details:
#             input_job_detail(job_detail, state)
#     except:
#         Log.log_message("FAILED TO INPUT")
#         with open(cwd+'/log.txt', 'a') as f:
#             f.write("FAILED TO INPUT DATA \n")
#         f.close()
