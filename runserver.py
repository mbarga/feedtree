#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import settings

pypath = os.environ["PYTHONPATH"]
sys.path.append(pypath)
print "Using python path: " + pypath
print "Using client secret: " + settings.FEEDLY_CLIENT_SECRET

from newstree import app

if __name__ == '__main__':
    # flask initialization
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)
    print "\n\n visit http://localhost:8080/auth"
