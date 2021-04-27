                            #### SERVER CHECKER - REQUESTS ####

import sys
import requests

if len(sys.argv) != 2:
    print('Too Many Or Not Enough Arguments Error')
    sys.exit(1)

server_addr = sys.argv[1]

try:
    reply = requests.head(server_addr)
except requests.RequestException:
    print('Communication Error')
else:
    if reply.status_code == requests.codes.ok:
        print(f'Website: {server_addr} is Live!')
        print(f'Response code: {reply.status_code}')
        print(reply.headers['Content-Type'])
    else:
        print('Server-Error')