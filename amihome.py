# Please set the address and HTTPS post data.  If you don't need the HTTPS post, comment out lines 16 and 17.

import os
import requests
import time

home = 0
address = "192.168.1.143"
y = 'y'

while y == 'y':
    response = os.system("ping -c 4 " + address)
    if response == 0:
        print address, 'is up!'
        if (home == 0):
            res = requests.post('Insert HTTPS Post Here', data='')
            print res
            home = 1
            print home
            time.sleep(1800)
    else:
        print address, 'is down!'
        #if (home == 1):
            #res = requests.post('Optional Secondary HTTPS Post', data='')
            #print res
            #home = 0
            #print home
            #time.sleep(10)
    time.sleep(10)
