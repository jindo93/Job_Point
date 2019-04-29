import os
import csv
import json

cwd = os.getcwd()


def make_dir_in_cwd(file_name):
    if not os.path.isdir(cwd + '/' + file_name):
        os.mkdir(cwd + '/' + file_name)
    return os.path.isdir(cwd + '/' + file_name)


def make_datafile_dir():
    return make_dir_in_cwd('datafile')


def make_logfile_dir():
    return make_dir_in_cwd('logfile')


def log_message(message):
    with open(cwd + '/logfile/log.txt', 'a') as f:
        f.write(message + '\n')
    f.close()
    return None


def instantiate_csv(name):
    columns = ["job_title", "post_url", "company", "location", "summary"]
    with open(cwd + '/datafile/{name}.csv'.format(name=name), 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(columns)
    f.close()
    return None


def job_data_to_csv(job_details, state):
    ''' CSV Format:
        job_title, job_post_url, company, location, summary
    '''
    with open(cwd + '/datafile/{state}.csv'.format(state=state), 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(job_details)
    f.close()
    return None
