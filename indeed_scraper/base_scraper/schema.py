#!/usr/bin/env python3

from py2neo import Node, Relationship


def input_job_data(graph, job_details):
    for job_detail in job_details:
        job = Node("Job", name=job_detail[0], post_url=job_detail[1])
        company = Node("Company", name=job_detail[2])
        location = Node("Location", name=job_detail[3])

        graph.merge(job, "Job", "post_url")
        graph.merge(company, "Company", "name")
        graph.merge(location, "Location", "name")
        HAS = Relationship.type("HAS")
        LOCATED = Relationship.type("LOCATED")
        graph.merge(HAS(company, job) | LOCATED(company, location))
