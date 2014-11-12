#!/usr/bin/env python
import tempfile
import webbrowser
import requests
import sys
import os
s = os.environ.get('DOT_FILE_VIZ_SERVER', 'http://127.0.0.1:6543')
url = s + '/dot'
fn = sys.argv[1]
resp = requests.post(url, files={'dot': open(fn, 'rb')})
fd, fn = tempfile.mkstemp() # deleted when goes out of scope (closed)
os.write(fd, resp.text)
os.fsync(fd)
print resp.text
webbrowser.open_new_tab(fn)
print 'You need to remove {f} if you are concerned about wasting storage'.format(f=fn)



