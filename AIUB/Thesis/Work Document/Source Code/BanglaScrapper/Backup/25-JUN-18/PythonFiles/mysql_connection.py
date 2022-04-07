'''
Title:              MySQL connection interface
Author:             Mehedi, Zarin, Dipanjan
Created:            23-JUN-2018, 07:31 PM
Last modified:      25-JUN-2018, 1:20 PM
Last modified by:   Dipanjan
'''

# -*- coding: utf-8 -*-
import mysql.connector as myconn
from mysql.connector import Error, errorcode, errors

config = {
    'user'             : 'root',
    'password'         : '',
    'host'             : 'localhost',
    'port'             : '3306',
    'database'         : 'testdb',
    'raise_on_warnings': True,
    'buffered'         : True }


def mysql_connection_func(sql_paragraph, sql_source_name, sql_date, sql_user_id, sql_domain_id, sql_source_link,
                          sql_sentence_count, sentence_dictionary):
    try:
        connection_string = myconn.connect(**config)
        # connection_string = myconn.connect(user='root', password='', host='localhost', database='banglascrapper',
        #                                    buffered=True)
        if connection_string.is_connected():
            print('successfully connected')

        cur = connection_string.cursor()

        insert_into_article = ('INSERT INTO article'
                               '(news_string, source, date, user_id, domain_id, source_link, sentence_count) '
                               'VALUES(%(news_string)s, %(source)s, %(date)s, %(u_id)s, %(domain_id)s, %(source_link)s, %(sentence_count)s)')


        select_into_article = ('SELECT source_link FROM article')
        cur.execute(select_into_article)
        rowk = cur.fetchone()
        while rowk is not None:
            if rowk[0] == sql_source_link:
                print('milse')
                # raise Exception(Error())
            # print(rowk[0])
            rowk = cur.fetchone()

        # insert_into_article = ("INSERT INTO article"
        #                "(news_string, source, date, user_id, domain_id, source_link, sentence_count)"
        #                "VALUES(%s, %s, %s, %s, %s, %s, %s)")

        # insert_into_article = ("INSERT INTO article"
        #                        "(news_string, source, date, user_id, domain_id, source_link, sentence_count)"
        #                        "VALUES(%d, %s, %s, %s, %d, %d, %s, %d)")

        # article_values = ('abc', 'def', '2015-06-12')
        # article_values = (sql_paragraph, sql_source_name, sql_date, sql_user_id, sql_domain_id, sql_source_link, sql_sentence_count)
        article_values = {
            'news_string'   : sql_paragraph,
            'source'        : sql_source_name,
            'date'          : sql_date,
            'u_id'          : sql_user_id,
            'domain_id'     : sql_domain_id,
            'source_link'   : sql_source_link,
            'sentence_count': sql_sentence_count }
        cur.execute(insert_into_article, article_values)
        connection_string.commit()


        cur.execute('select max(id) from article')
        rowl = cur.fetchone()

        for (a, b) in sentence_dictionary.items():
            print(a)
            insert_into_article_line = ('INSERT INTO article_line'
                                        # '(sentence, article_id, is_visited, is_answered, is_justified, word_count, user_id) '
                                        '(sentence, article_id, word_count, user_id) '
                                        'VALUES(%(sentence_string)s, %(article_id)s, %(word_count)s, %(user_id)s)')
                                        # 'VALUES(%(sentence_string)s, %(article_id)s, %(is_visited)s, %(is_answered)s, %(is_justified)s, %(word_count)s, %(user_id)s)')

            article_line_values = {
                'sentence_string': a,
                'article_id'     : rowl[0],
                # 'is_visited'     : 0,
                # 'is_answered'    : 0,
                # 'is_justified'   : 0,
                'word_count'     : b,
                'user_id'        : sql_user_id }

            cur.execute(insert_into_article_line, article_line_values)
        connection_string.commit()
    except Error as e:
        print(e)


    finally:
        cur.close()
        connection_string.close()

        return

# mysql_connection()
