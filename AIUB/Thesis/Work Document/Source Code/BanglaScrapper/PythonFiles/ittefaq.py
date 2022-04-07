'''
Title:              Web scraping from Ittefaq
Author:             Mehedi, Zarin, Dipanjan
Created:            08-MAY-2018, 10:35 AM
Last modified:      26-JUN-2018, 12:01 AM
Last modified by:   Dipanjan
'''

# -*- coding: utf-8 -*-
from PythonFiles import change_time_format, mysql_connection
import urllib3
import re
from bs4 import BeautifulSoup as soup
import datetime

my_url = 'http://www.ittefaq.com.bd/print-edition/sports-news/2018/06/01/280708.html'  # page source link
# my_url = 'http://www.ittefaq.com.bd/print-edition/sports-news/2018/05/05/274956.html'  # page source link
# my_url = 'http://www.ittefaq.com.bd/print-edition/sports-news/2016/01/03/93120.html'

http = urllib3.PoolManager()
uagent = http.request(
        'GET',
        my_url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
            }
        )  # create user agent for parsing the source

page_html = uagent.data
page_soup = soup(page_html, "html.parser")
article_body = page_soup.findAll("div", { "class": "details" })  # select article paragraph
article_title = page_soup.findAll("div", { "class": "headline2" })  # select article title
article_date = page_soup.findAll("span", { "class": "entrytime" })  # select article date

# article_title_top = page_soup.findAll("div", {"class": "headline1"})  # supporting article title
# article_title_middle = page_soup.findAll("div", {"class": "headline2"})  # main article title
# article_title_bottom = page_soup.findAll("div", {"class": "headline3"})  # supporitng article title


# for x in page_soup.find('div', {'class': 'details'}).find_all('div'):
#     print(x.text)

dick = { }
sentence_dictionary = { }
article_sentence_count = 0
sentence_word_count = 0
paragraph_text = ''
for a in article_body:
    article_paragraph = a.findAll("div")  # find all existing body paragraph text
    if len(article_paragraph) <= 1:  # if list of article paragraph less than 1 then switch to another parser
        article_paragraph = a.findAll("p", { "class": "MsoNormal" })  # find all existing body paragraph text
    else:  # else continue as usual decleration
        article_paragraph = article_paragraph

    print(len(article_paragraph))
    # del article_paragraph[-1:]    # remove last element from list
    # print (*article_paragraph, sep='\n')
    for b in article_paragraph:
        # paragraph_text = paragraph_text + x.text
        c = b.text  # contains the text
        c = c.split('।')  # split article paragraph for sentence count
        c = [str for str in c if str]  # removing empty spaces from list
        del c[-1:]  # removing &nbsp tag from last index
        # print(c)  # print list of sentences
        # print(b)  # print article tags
        for d in c:
            article_sentence_count += 1
            u = article_sentence_count
            print(u, d)  # print article lines
            paragraph_text = paragraph_text + d + '।'  # formatting text for sql queries
            # print(len(d))  # print number of letter in a sentence
            e = d.split(" ")  # split sentence for word count
            # print(e)
            del e[0]
            sentence_word_count = len(e)  # count no of word in a sentence
            print(sentence_word_count)
            sentence_dictionary.update({ d: sentence_word_count })

# print(article_date[0].text)  # print article source date
formatted_time = re.split(',| |ইং', article_date[0].text)  # regular expression to split bangla date
formatted_time = [str for str in formatted_time if str]  # remove blank index from list
temp_date = list(formatted_time[2])  # split bangla year into a list
#
# aDate, aMonth, aYear = change_time_format.convert_time(formatted_time[0], formatted_time[1],
#                                                        temp_date)  # convert bangla date ennglish
fetch_date = change_time_format.convert_time(formatted_time[0], formatted_time[1],
                                             temp_date)  # convert bangla date ennglish

sql_article_title = article_title[0].text  # sql query titile
sql_news_string = paragraph_text  # sql query article body
sql_source_name = 'Ittefaq'  # sql query source name
sql_source_name_id = 3
sql_date_added = fetch_date  # sql query date
sql_user_id = 1
sql_domain_id = 3
sql_source_link = my_url  # sql query source link
sql_sentence_count = article_sentence_count
sql_date_updated = datetime.date.today()

# sql_date = str(aYear) + '-' + str(aMonth) + '-' + str(aDate)  # sql query date

print(sql_news_string)
print(sql_source_name)
print(sql_date_added)
print(sql_user_id)
print(sql_domain_id)
print(sql_source_link)
print(sql_article_title)
print(sql_sentence_count)
print(sql_date_updated)

mysql_connection.mysql_connection_func(sql_article_title, sql_news_string, sql_source_name_id, sql_date_added,
                                       sql_user_id, sql_domain_id, sql_source_link, sql_sentence_count,
                                       sql_date_updated, sentence_dictionary)
# print (div.find('a').contents[0])           """ --------------------------------- ""
# print (div.find('img')['src'])              """ |   some useful object elements | """
# print (article_body[0].div.div.p)           """ --------------------------------- """

a = 1
b = 6
s = 2
c = 11
dict = { (a): (b), (s): (c) }
# print(dick.items())

# for a, b in sentence_dictionary.items():
#     print(a,b)

# print(len(dick))
