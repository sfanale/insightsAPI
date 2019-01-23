from datetime import datetime
import psycopg2

import flask


# 3rd party modules
from flask import make_response, abort


def connect_to_db():
    """
    This function uses the psycopg2 library to connect to an RDS instance where the tables for this project are
    being stored. I currently have the information here and I should remove it.
    :return: cursor and connection objects for interacting with the table
    """
    try:
        conn = psycopg2.connect(host="options-prices.cetjnpk7rvcs.us-east-1.rds.amazonaws.com", database="options_prices",
                            user="Stephen", password="password69")
        cur = conn.cursor()
        return cur, conn
    except ConnectionRefusedError:
        return "Connection Refused"


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def getAllBlogs():
    """
    This function currently just gets all blogs. I will probably add an input to this in the future so you only retrieve
    blogs of a certain type. That this same code can be used for accessing the educational materials.

    :return: Returns list of all blogs
    """
    cur, conn = connect_to_db()
    cur.execute("""SELECT author, date, title, description, content, tags, image, views, id from insights;""",)
    all = cur.fetchall()
    response = []
    for result in all:
        response.append({'author': result[0], 'date': result[1], 'title': result[2], 'description':result[3], 'content': result[4],
        'tags': result[5], 'imgae': result[6], 'views': result[7], 'id':result[8]})
    cur.close()
    conn.close()
    return flask.jsonify(response)


def getAllLearn():
    """
    This function currently just gets all blogs. I will probably add an input to this in the future so you only retrieve
    blogs of a certain type. That this same code can be used for accessing the educational materials.

    :return: Returns list of all blogs
    """
    cur, conn = connect_to_db()
    cur.execute("""SELECT title, description, content, tags, image, id from learn;""",)
    all = cur.fetchall()
    response = []
    for result in all:
        response.append({'title': result[0], 'description':result[1], 'content': result[2],
        'tags': result[3], 'image': result[4], 'id':result[5]})
    cur.close()
    conn.close()
    return flask.jsonify(response)



def getOneBlog(id):
    cur, conn = connect_to_db()
    try:
        cur.execute("""SELECT author, date, title, description, content, tags, image, views, id from insights WHERE id=%s;""", id)

        result = cur.fetchall()[0]
        response = {'author': result[0], 'date': result[1], 'title': result[2], 'description':result[3], 'content': result[4],
            'tags': result[5], 'image': result[6], 'views': result[7], 'id': result[8]}
    except KeyError or ValueError:
        abort(
            404, "page with name {id} not found".format(id=id)
        )
    cur.close()
    conn.close()
    return flask.jsonify(response)

def getOneLearn(id):
    cur, conn = connect_to_db()
    try:
        cur.execute("""SELECT title, description, content, tags, image, id from learn WHERE id=%s;""", id)

        result = cur.fetchall()[0]
        response = {'title': result[0], 'description':result[1], 'content': result[2],
            'tags': result[3], 'image': result[4], 'id': result[5]}
    except KeyError or ValueError:
        abort(
            404, "page with name {id} not found".format(id=id)
        )
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


def postLearn(body):
    cur, conn = connect_to_db()
    # write data to database
    print(body)
    cur.execute("""INSERT INTO learn (title, description, content, tags, image) VALUES (
        %(title)s, %(description)s, %(content)s, %(tags)s,%(image)s);""", body)
    # save addition
    conn.commit()
    cur.close()
    conn.close()

