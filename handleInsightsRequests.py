from datetime import datetime
import psycopg2

import flask


# 3rd party modules
from flask import make_response, abort


def connect_to_db():
    conn = psycopg2.connect(host="options-prices.cetjnpk7rvcs.us-east-1.rds.amazonaws.com", database="options_prices",
                            user="Stephen", password="password69")
    cur = conn.cursor()
    return cur, conn


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def getAllBlogs():
    cur, conn = connect_to_db()
    cur.execute("""SELECT author, date, title, description, content, tags, image, views, id from insights;""",)
    all = cur.fetchall()
    response = []
    print(all)
    for result in all:
        print(result)
        response.append({'author': result[0], 'data': result[1], 'title': result[2], 'description':result[3], 'content': result[4],
        'tags': result[5], 'imgae': result[6], 'views': result[7], 'id':result[8]})
    cur.close()
    conn.close()
    return flask.jsonify(response)



def getOneBlog(id):
    cur, conn = connect_to_db()
    cur.execute("""SELECT author, date, title, description, content, tags, image, views, id from insights WHERE id=%s;""", id)
    result = cur.fetchall()[0]
    response = {'author': result[0], 'data': result[1], 'title': result[2], 'description':result[3], 'content': result[4],
        'tags': result[5], 'imgae': result[6], 'views': result[7], 'id': result[8]}
    cur.close()
    conn.close()
    return flask.jsonify(response)


def postBlog(body):
    cur, conn = connect_to_db()
    # write data to database
    print(body)

    cur.execute("""INSERT INTO insights (author, date, title, description, content, tags, image) VALUES (%(author)s, %(date)s,
        %(title)s, %(description)s, %(content)s, %(tags)s,%(image)s);""", body)
    # save addition
    conn.commit()
    cur.close()
    conn.close()

