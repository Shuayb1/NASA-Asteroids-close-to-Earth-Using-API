from flask import Flask, render_template
from flask_pymongo import PyMongo

import operator
from nasaDB import TheClient
from nasaApi import TheAPI

from envparse import env
env.read_envfile()
mongodb_server = env.str('MONGODB_SERVER')

app = Flask(__name__)
app.config['MONGO_DB'] = TheClient
app.config['MONGO_URI'] = mongodb_server

mongo = PyMongo(app)


@app.route('/')
def index():
    # get the newest document by sorting in descending order
    document_cursor_today = mongo.db.nasa_collections_today.find({}, {'_id': False}).sort('_id', -1).limit(1)

    iterated_doc_today = []

    # get the newest document and sort the values
    for doc_today in document_cursor_today:
        sorted_doc_today = sorted(doc_today.items())
        sorted_doc_today.sort(key=operator.itemgetter(1))

        # iterate over the sorted document
        for numbering_today, (asteroid_name_today, asteroid_distance_today) in enumerate(sorted_doc_today):

            if numbering_today < 5:
                iterated_doc_today.append({"i": numbering_today + 1, "key": asteroid_name_today,
                                           "value": asteroid_distance_today})
    return render_template('nasa.html', iterated_doc_today=iterated_doc_today, end_date=TheAPI.end_date,
                           start_date=TheAPI.start_date)


@app.route('/sevenDaysUpdate')
def seven_days():

    # get the newest document by sorting in descending order
    document_cursor = mongo.db.nasa_collections.find({}, {'_id': False}).sort('_id', -1).limit(1)

    #get the newest document and sort the values
    fields = {}
    a = {}

    for doc in document_cursor:

        for key, value in doc.items():

            sorted_doc = sorted(value.items())
            sorted_doc.sort(key=operator.itemgetter(1))

            fields[key] = sorted_doc

    for i, k in fields.items():

        limited_array = fields[i][:5]
        lall = []

        count = 0
        for c in limited_array:
            count += 1
            # lall.append(''.join('asteroid' + c[0] + ' distance' + c[1]))
            lall.append({'count': count, 'name': c[0], 'distance': c[1]})
            a[i] = lall
    print(a)
    return render_template('sevenDaysUpdate.html', fields=fields, a=a)


if __name__ == '__main__':
    app.run(debug=True)
