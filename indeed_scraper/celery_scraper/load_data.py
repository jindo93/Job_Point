#!/usr/bin/env python3

from neo4j import GraphDatabase
import requests
import json
import os
import csv
import logger as Log

from auth import URL, NEO4J_USR, NEO4J_PW

driver = GraphDatabase.driver(URL, auth=(NEO4J_USR, NEO4J_PW))


def load_MI():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/MI.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: MI.csv")
        return None
    except:
        Log.log_message("Failed importing: MI.csv")
        return None

def load_MN():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/MN.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: MN.csv")
        return None
    except:
        Log.log_message("Failed importing: MN.csv")
        return None

def load_MO():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/MO.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: MO.csv")
        return None
    except:
        Log.log_message("Failed importing: MO.csv")
        return None

def load_MS():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/MS.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: MS.csv")
        return None
    except:
        Log.log_message("Failed importing: MS.csv")
        return None

def load_MT():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/MT.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: MT.csv")
        return None
    except:
        Log.log_message("Failed importing: MT.csv")
        return None

def load_NC():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NC.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NC.csv")
        return None
    except:
        Log.log_message("Failed importing: NC.csv")
        return None

def load_ND():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/ND.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: ND.csv")
        return None
    except:
        Log.log_message("Failed importing: ND.csv")
        return None

def load_NE():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NE.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NE.csv")
        return None
    except:
        Log.log_message("Failed importing: NE.csv")
        return None

def load_NH():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NH.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NH.csv")
        return None
    except:
        Log.log_message("Failed importing: NH.csv")
        return None

def load_NJ():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NJ.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NJ.csv")
        return None
    except:
        Log.log_message("Failed importing: NJ.csv")
        return None

def load_NM():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NM.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NM.csv")
        return None
    except:
        Log.log_message("Failed importing: NM.csv")
        return None

def load_NV():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NV.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NV.csv")
        return None
    except:
        Log.log_message("Failed importing: NV.csv")
        return None

def load_NY():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/NY.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: NY.csv")
        return None
    except:
        Log.log_message("Failed importing: NY.csv")
        return None

def load_OH():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/OH.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: OH.csv")
        return None
    except:
        Log.log_message("Failed importing: OH.csv")
        return None

def load_OK():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/OK.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: OK.csv")
        return None
    except:
        Log.log_message("Failed importing: OK.csv")
        return None

def load_OR():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/OR.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: OR.csv")
        return None
    except:
        Log.log_message("Failed importing: OR.csv")
        return None

def load_PA():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/PA.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: PA.csv")
        return None
    except:
        Log.log_message("Failed importing: PA.csv")
        return None

def load_RI():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/RI.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: RI.csv")
        return None
    except:
        Log.log_message("Failed importing: RI.csv")
        return None

def load_SC():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/SC.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: SC.csv")
        return None
    except:
        Log.log_message("Failed importing: SC.csv")
        return None

def load_SD():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/SD.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: SD.csv")
        return None
    except:
        Log.log_message("Failed importing: SD.csv")
        return None

def load_TN():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/TN.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: TN.csv")
        return None
    except:
        Log.log_message("Failed importing: TN.csv")
        return None

def load_TX():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/TX.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: TX.csv")
        return None
    except:
        Log.log_message("Failed importing: TX.csv")
        return None

def load_UT():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/UT.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: UT.csv")
        return None
    except:
        Log.log_message("Failed importing: UT.csv")
        return None

def load_VA():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/VA.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: VA.csv")
        return None
    except:
        Log.log_message("Failed importing: VA.csv")
        return None

def load_VT():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/VT.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: VT.csv")
        return None
    except:
        Log.log_message("Failed importing: VT.csv")
        return None

def load_WA():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/WA.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: WA.csv")
        return None
    except:
        Log.log_message("Failed importing: WA.csv")
        return None

def load_WI():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/WI.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: WI.csv")
        return None
    except:
        Log.log_message("Failed importing: WI.csv")
        return None

def load_WV():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/WV.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: WV.csv")
        return None
    except:
        Log.log_message("Failed importing: WV.csv")
        return None

def load_WY():
    try:
        with driver.session() as session:
            session.run(
                "LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/jindo93/job_data/master/datafiles/WY.csv' "
                "AS row FIELDTERMINATOR '\t'"
                "CREATE (j:Job {name: row.job_title, summary: row.summary, post_url: row.post_url})"
                "MERGE (c:Company {name: row.company})"
                "MERGE (l:Location {name: row.location})"
                "MERGE (l)<-[:LOCATED]-(j)<-[:HAS]-(c)"
            )
        session.close()
        Log.log_message("Succeeded importing: WY.csv")
        return None
    except:
        Log.log_message("Failed importing: WY.csv")
        return None