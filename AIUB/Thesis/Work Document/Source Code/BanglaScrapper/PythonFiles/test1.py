# -*- coding: utf-8 -*-
import mysql.connector as myconn
from mysql.connector import Error, errorcode, errors
import datetime
x=datetime.date.today()

print (x)
# config = {
#     'user'             : 'root',
#     'password'         : '',
#     'host'             : 'localhost',
#     'port'             : '3306',
#     'database'         : 'banglascrapper-test1',
#     'raise_on_warnings': True,
#     'buffered'         : True }
# try:
#     connection_string = myconn.connect(**config)
#     if connection_string.is_connected():
#         print('successfully connected')
#
#     qu = '''
# SELECT DISTINCT
#   word.article_line_id,
#   word_annotation_justifiers.is_answered,
#   word.word_string,
#   word_annotation_justifiers.word_id
#   FROM
#   word_annotation_justifiers
#   INNER JOIN word ON word_annotation_justifiers.word_id = word.id
#   INNER JOIN article_line ON word.article_line_id = article_line.id
#   WHERE
#   word.article_line_id = 1 AND
#   word_annotation_justifiers.is_answered = 1'''
#
#     cur = connection_string.cursor()
#     select_into_test_table = qu
#     cur.execute(qu)
#
#     row = cur.rowcount
#     # row = cur.fetchall()
#     print(row)
#
#     r = cur.fetchall()
#
#     for i in r:
#         print(i[2])
#
# except Error as e:
#     print(e)
#
# finally:
#     cur.close()
#     connection_string.close()
