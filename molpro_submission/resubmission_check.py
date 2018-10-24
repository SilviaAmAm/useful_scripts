"""
This script reads the file containing the indices of the jobs that have crashed and re-submits them.
"""

import os
import time
import numpy as np

######### Things to change ################
file_with_crashed = "crashed_jobs.txt"
max_n_jobs = 10
###########################################

indices = np.genfromtxt(file_with_crashed, delimiter=",", dtype=np.int32)[:-1]

counter = 0
tot_jobs = len(indices)
jobs_to_go = tot_jobs - counter

while jobs_to_go > 0:

    if counter == tot_jobs-1:
        exit()

    n_jobs_in_queue = os.popen('qstat -u sa16246 | wc -l').read()
    n_jobs_in_queue = int(n_jobs_in_queue.strip())

    if n_jobs_in_queue < max_n_jobs:
        n_jobs_to_submit = max_n_jobs - n_jobs_in_queue

        if n_jobs_to_submit > jobs_to_go:
            n_jobs_to_submit = jobs_to_go

        for i in range(n_jobs_to_submit):
            os.system("python resubmission_script.py %i " % (indices[counter+i]))

        counter += n_jobs_to_submit

    jobs_to_go = tot_jobs - counter

    time.sleep(600)