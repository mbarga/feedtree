# -*- coding: UTF-8 -*-

from settings import db
from flask import Blueprint
from flask import render_template

visual = Blueprint('visual', __name__,
                   template_folder='templates',
                   static_folder='static')


@visual.route('/test', methods=['GET'])
#TODO: throws exception when DB is empty
def test():
    keys = db.keys()
    entries_raw = db.mget(keys)
    entries = []
    for entry in entries_raw:
        temp_dict = eval(entry)
        entries.append(temp_dict)
    #TODO: not all entries have an engagement field
    with_eng = [entry for entry in entries if 'engagement' in entry]
    with_eng.sort(key=lambda x: x["engagement"])
    return render_template('newstree.html', entries=with_eng)
