'''
Title:              MySQL connection interface
Author:             Mehedi, Zarin, Dipanjan
Created:            23-JUN-2018, 07:31 PM
Last modified:      08-JUL-2018, 1:20 PM
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
    'database'         : 'banglascrapper_final1',
    'raise_on_warnings': True,
    'buffered'         : True }


def mysql_connection_func(sql_article_title, sql_news_string, sql_source_name_id, sql_date_added, sql_user_id,
                          sql_domain_id, sql_source_link, sql_sentence_count, sql_date_updated, sentence_dictionary):
    try:
        connection_string = myconn.connect(**config)
        if connection_string.is_connected():
            print('successfully connected')

        cur = connection_string.cursor()

        insert_into_article = ('INSERT INTO article'
                               '(article_title, news_string, source_name_id, date_added, user_id, domain_id, source_link, sentence_count) '
                               'VALUES(%(article_title)s, %(news_string)s, %(source_name_id)s, %(date_added)s, %(user_id)s, %(domain_id)s, %(source_link)s, %(sentence_count)s)')

        article_values = {
            'article_title' : sql_article_title,
            'news_string'   : sql_news_string,
            'source_name_id': sql_source_name_id,
            'date_added'    : sql_date_added,
            'user_id'       : sql_user_id,
            'domain_id'     : sql_domain_id,
            'source_link'   : sql_source_link,
            'sentence_count': sql_sentence_count }
        cur.execute(insert_into_article, article_values)
        connection_string.commit()

        cur.execute('select max(id) from article')
        next_id = cur.fetchone()

        for (sentence_string, word_count) in sentence_dictionary.items():
            # print(sentence_string)
            insert_into_article_line = ('INSERT INTO article_line'
                                        '(sentence_string, article_id, is_visited, is_answered, is_justified, word_count, user_id, date_updated) '
                                        'VALUES(%(sentence_string)s, %(article_id)s, %(is_visited)s, %(is_answered)s, %(is_justified)s, %(word_count)s, %(user_id)s, %(date_updated)s)')

            article_line_values = {
                'sentence_string': sentence_string,
                'article_id'     : next_id[0],
                'is_visited'     : 0,
                'is_answered'    : 0,
                'is_justified'   : 0,
                'word_count'     : word_count,
                'user_id'        : sql_user_id,
                'date_updated'   : sql_date_updated }

            cur.execute(insert_into_article_line, article_line_values)
        connection_string.commit()

    except Error as e:
        print(e)

    finally:
        cur.close()
        connection_string.close()

        return

# mysql_connection()
