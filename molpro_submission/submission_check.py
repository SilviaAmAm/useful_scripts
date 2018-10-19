import os
import time

######### Things to change ################
max_n_jobs = 50
tot_jobs = 40604
counter = 609        # The index of the next job to do
###########################################

jobs_to_go = tot_jobs - counter

while jobs_to_go > 0:

    if counter == tot_jobs-1:
        exit()

    n_jobs_in_queue = os.popen('ls -l *.py | wc -l').read()
    n_jobs_in_queue = int(n_jobs_in_queue.strip())

    if n_jobs_in_queue < max_n_jobs:
        n_jobs_to_submit = max_n_jobs - n_jobs_in_queue

        if n_jobs_to_submit > jobs_to_go:
            n_jobs_to_submit = jobs_to_go

        os.system("python submission_script.py %i %i" % (counter, counter+n_jobs_to_submit))

        counter += n_jobs_to_submit

    jobs_to_go = tot_jobs - counter

    time.sleep(600)