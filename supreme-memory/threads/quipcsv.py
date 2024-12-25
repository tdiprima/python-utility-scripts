"""
Create your own error.  Trying stuff to exit from the pool.
"""
import os
import signal
import sys
from multiprocessing import Pool
from subprocess import Popen, PIPE

import requests

pathdb = False
pdb = {}


class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    try:
        _id = ""
        if pathdb:
            get_image_id(mdata["case_id"])
            _id = get_slide_unique_id()
            if is_blank(_id):
                print('Slide not found ' + pdb["imageid"])
    except MyError as me:
        print('helloooo', me)
        sys.exit(1)  # abort


def get_auth_token():
    '''
    get an auth token
    '''
    endpoint = pdb["url"] + '/jwt/token'
    response = requests.get(endpoint, auth=(pdb["user"], pdb["passwd"]))
    if response.status_code == 403:
        raise MyError('Error getting token. status_code was: {}'.format(response.status_code))
    else:
        response = response.json()
        token_string = response['token']

    return token_string


if __name__ == "__main__":

    mfiles = []
    if len(mfiles) == 0:
        print('There are no files to process.')
    else:
        p = Pool(processes=2)
        try:
            p.map(process_quip, mfiles, 1)
        except MyError as me:
            for process in p:
                processId = process.pid
                print("attempting to terminate " + str(processId))
                command = " ps -o pid,ppid -ax | grep " + str(processId) + " | cut -f 1 -d \" \" | tail -1"
                ps_command = Popen(command, shell=True, stdout=PIPE)
                ps_output = ps_command.stdout.read()
                retcode = ps_command.wait()
                assert retcode == 0, "ps command returned %d" % retcode
                print("child process pid: " + str(ps_output))
                os.kill(int(ps_output), signal.SIGTERM)
                os.kill(int(processId), signal.SIGTERM)
            # p.close()
            # p.terminate()
            # p.join()

