#!/usr/bin/env python3

from neo4j import GraphDatabase
import logger as Log

from auth import URL, NEO4J_USR, NEO4J_PW


driver = GraphDatabase.driver(URL, auth=(NEO4J_USR, NEO4J_PW))


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
