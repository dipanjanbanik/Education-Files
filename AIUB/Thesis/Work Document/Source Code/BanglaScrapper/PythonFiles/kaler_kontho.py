'''
Title:              Web scraping from Ittefaq
Author:             Mehedi, Zarin, Dipanjan
Created:            08-MAY-2018, 10:35 AM
Last modified:      16-MAY-2018, 09:09 PM
Last modified by:   Dipanjan
'''

# -*- coding: utf-8 -*-
from PythonFiles import change_time_format
import urllib3
import re
from bs4 import BeautifulSoup as soup


def remove_string(contain_string, contain_list):
    dx = 0
    for a in contain_list:
        if a == contain_string:
            del contain_list[dx]
        dx += 1
    return contain_list


# my_url = 'http://www.kalerkantho.com/print-edition/sports/2018/04/30/630916'  # page source link
# my_url = 'http://www.kalerkantho.com/print-edition/sports/2018/04/30/630930'  # page source link
my_url = 'http://www.kalerkantho.com/print-edition/sports/2018/06/25/650641'

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
article_body = page_soup.findAll("div", { "class": "some-class-name2" })  # select article paragraph
article_title = page_soup.findAll("div", { "class": "col-sm-12 col-md-8 details" })  # select article title
article_date = page_soup.findAll("p", { "class": "text-left pull-left n_author" })  # select article date

# article_title_top = page_soup.findAll("div", {"class": "headline1"})  # supporting article title
# article_title_middle = page_soup.findAll("div", {"class": "headline2"})  # main article title
# article_title_bottom = page_soup.findAll("div", {"class": "headline3"})  # supporitng article title

# for x in page_soup.find('div', {'class': 'col-sm-12 col-md-8 details'}).find_all('h2'):
#     print(x.text)

for a in article_title:
    b = a.findAll("h2")  # html tag element contains article title
    for c in b:
        d = c.text  # contains article title text
        print(d)  # print article title

# print(article_title[0].text)
letter_count = 0
dick = { }
article_sentence_count = 0
sentence_word_count = 0
paragraph_text = ''
result = []
for a in article_body:
    article_paragraph = a.findAll("p")  # find all existing body paragraph text
    # del article_paragraph[-1:]    # remove last element from list
    # print (*article_paragraph, sep='\n')
    for b in article_paragraph:
        # paragraph_text = paragraph_text + x.text
        c = b.text
        c = c.split('।')  # split article paragraph for sentence count
        # c = [str for str in c if str]  # removing empty spaces from list
        # del c[-1:]  # removing &nbsp tag from last index
        # print(c)  # print list of sentences
        # print(b)  # print article tags
        for d in c:
            article_sentence_count += 1
            u = article_sentence_count
            print(d)  # print article lines
            paragraph_text = paragraph_text + d + '।'  # formatting text for sql queries
            letter_count = letter_count + len(d)
            print(len(d)-1)  # print number of letter in a sentence
            e = d.split(" ")  # split sentence for word count
            # print(e)
            # del e[0]  #no need this part
            # dx = 0
            # for f in e:
            #     if f == '‘':
            #         del e[dx]
            #     dx += 1
            #
            # dx = 0
            # for f in e:
            #     if f == '’':
            #         del e[dx]
            #     dx += 1
            #
            # dx = 0
            # for f in e:
            #     if f == '':
            #         del e[dx]
            #     dx += 1

            remove_string('', e)
            remove_string('‘', e)
            remove_string('‘‘‘', e)
            remove_string('’', e)
            remove_string('’’', e)

            if len(e) == 0:
                continue

                # print(e[f])

                # else:
                #     print(len(e)) #no need else part
            # if e[0]=='':
            #     # print("blank paisi")
            #     del e[0]
            # # else:
            # #     print(len(e)) #no need else part
            sentence_word_count = len(e)
            # print(e)

            # print(e, sentence_word_count)
            dick.update({ (u): (sentence_word_count) })

# print(article_date[0].text)  # print article source date
formatted_time = re.split(',| ', article_date[1].text)  # regular expression to split bangla date
formatted_time = [str for str in formatted_time if str]  # remove blank index from list
temp_date = list(formatted_time[2])  # split bangla year into a list

# aDate, aMonth, aYear = change_time_format.convert_time(formatted_time[0], formatted_time[1],
#                                                        temp_date)  # convert bangla date ennglish

temp = change_time_format.convert_time(formatted_time[0], formatted_time[1],
                                       temp_date)  # convert bangla date ennglish

# print(formatted_time[1])

sql_source_name = 'Kaler Kontho'  # sql query source name
sql_source_link = my_url  # sql query source link
sql_title = article_title[0].text  # sql query titile
# sql_date = str(aYear) + '-' + str(aMonth) + '-' + str(aDate)  # sql query date
sql_date = temp
sql_paragraph = paragraph_text  # sql query article body
sql_sentence_count = article_sentence_count

# print(sql_source_name)
# print(sql_source_link)
# print(sql_title)
print(sql_date)
# print(sql_paragraph)
# print(sql_sentence_count)
# print (div.find('a').contents[0])           """ --------------------------------- ""
# print (div.find('img')['src'])              """ |   some useful object elements | """
# print (article_body[0].div.div.p)           """ --------------------------------- """
print(letter_count)

a = 1
b = 6
s = 2
c = 11
dict = { (a): (b), (s): (c) }
# print(len(dick))
