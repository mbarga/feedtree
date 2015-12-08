#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

pypath = os.environ["PYTHONPATH"]
sys.path.append(pypath)
print "Using python path: " + pypath

from newstree import app

if __name__ == '__main__':
    # flask initialization
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)
