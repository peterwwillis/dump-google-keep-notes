#!/usr/bin/env python
import gkeepapi
import netrc
import sys
import os
import json

username, password = None, None

rc = netrc.netrc(os.environ.get('NETRC'))
try:
    login = rc.authenticators("google.com")
    if login:
        username, _, password = login
except:
    pass

if not username or not password:
    if len(sys.argv) < 3:
        print("Error: please pass Google Keep username and password")
        sys.exit(1)
    username, password = sys.argv[1], sys.argv[2]

keep = gkeepapi.Keep()
success = keep.login(username, password)

state = keep.dump()
fh = open('google_keep_state.json', 'w')
json.dump(state, fh)
