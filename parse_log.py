#!/user/bin/env python3

import sys
import re

ptn = re.compile(
    '^[A-Z]+ '
    '(?P<date_time>\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}),.+'
    'Authenticated user: (?P<auth_user>[\w]{2,})\..+'
    'Local name: (?P<local_name>\w{2,})\.')

while True:
    line = sys.stdin.readline()
    if not line:
        break
    if 'Authenticated user:' in line:
        m = re.match(ptn, line)
        try:
            sys.stdout.write('{},{},{}\n'.format(m.group('date_time'),
                m.group('auth_user'), m.group('local_name')))
            sys.stdout.flush()
        except:
            sys.stderr.write(line)
            sys.stderr.flush()