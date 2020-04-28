#!/usr/bin/env python
# Python 2 client that updates acme-dns TXT records (can be used with Win-Acme for example)
# author: OwN-3m-All <own3mall@gmail.com>
# dependencies:  sudo pip install requests or on Windows just pip install requests

############################
#  Imports                 #
############################

import requests  # the lib that handles the url stuff
from urllib3.exceptions import InsecureRequestWarning
import datetime
import threading
import sys
import os
import json
import time

############################
#  Variables               #
############################
acmeUsername = '{acme-dns-api-username}'
acmePassword = '{acme-dns-api-password}'
acmeUpdateURL = '{acme-dns-update-url}'
acmeSubdomain = '{acme-dns-api-subdomain}'

# Do not edit these variables
acmeDomain = sys.argv[2]
acmeChallenge = sys.argv[3]
acmeText = sys.argv[4]
logfile = sys.path[0] + "/acme-dns-update.log"
print("System arguments received" + str(sys.argv))

# Rotate log file if it's too large
if os.path.isfile(logfile):
	log_file_size = os.stat(logfile).st_size
	if log_file_size >= 20971520:
		os.rename(logfile, logfile + dtString)
	else:
		print("Logfile size is %s" % (str(log_file_size)) + "\n")

log_file = open(logfile,"a+")
sys.stdout = log_file

if acmeDomain and acmeChallenge and acmeText:
	print("Updating TXT DNS record for domain " + acmeDomain + " with the value of " + acmeText)
		
	headers = {'X-Api-User': acmeUsername, 'X-Api-Key': acmePassword}
	payload = {'subdomain': acmeSubdomain, 'txt': acmeText}

	r = requests.post(acmeUpdateURL, json=payload, headers=headers, verify=False)

	print(r)
