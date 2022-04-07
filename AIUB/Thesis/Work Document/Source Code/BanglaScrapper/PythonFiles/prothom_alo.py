'''
Title:              Web scraping from Prothom-Alo
Author:             Mehedi, Zarin, Dipanjan
Created:            24-NOV-2017, 10:35 AM
Last modified:      10-JAN-2018, 01:03 PM
Last modified by:   Dipanjan
'''


import codecs
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#article 1 - বন্ধুর সঙ্গে প্রতিযোগিতা!
#my_url = 'http://www.prothom-alo.com/life-style/article/1371196/%E0%A6%AC%E0%A6%A8%E0%A7%8D%E0%A6%A7%E0%A7%81%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF%E0%A6%AF%E0%A7%8B%E0%A6%97%E0%A6%BF%E0%A6%A4%E0%A6%BE'

#article 2 - নতুন সদস্য নিয়ে শিরোনামহীন
#my_url = 'http://www.prothom-alo.com/entertainment/article/1374341/%E0%A6%A8%E0%A6%A4%E0%A7%81%E0%A6%A8-%E0%A6%B8%E0%A6%A6%E0%A6%B8%E0%A7%8D%E0%A6%AF-%E0%A6%A8%E0%A6%BF%E0%A7%9F%E0%A7%87-%E0%A6%B6%E0%A6%BF%E0%A6%B0%E0%A7%8B%E0%A6%A8%E0%A6%BE%E0%A6%AE%E0%A6%B9%E0%A7%80%E0%A6%A8'

#article 3 - শতরঞ্জির বিশ্বজয়
#my_url = 'http://www.prothom-alo.com/economy/article/1368246/%E0%A6%B6%E0%A6%A4%E0%A6%B0%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%B0-%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%AC%E0%A6%9C%E0%A7%9F'#article 3 - শতরঞ্জির বিশ্বজয়

#article 4 - ‘বাবা’র ছড়াছড়ি যে শহরে
my_url = 'http://www.prothomalo.com/bangladesh/article/1405486/%E2%80%98%E0%A6%AC%E0%A6%BE%E0%A6%AC%E0%A6%BE%E2%80%99%E0%A6%B0-%E0%A6%9B%E0%A7%9C%E0%A6%BE%E0%A6%9B%E0%A7%9C%E0%A6%BF-%E0%A6%AF%E0%A7%87-%E0%A6%B6%E0%A6%B9%E0%A6%B0%E0%A7%87'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

print(page_html)

article_body    = page_soup.findAll("div", {"itemprop": "articleBody"})         #select article paragraph
article_title   = page_soup.findAll("div", {"class": "right_title"})            #select article title
article_author  = page_soup.findAll("div", {"class": "author each_row"})        #select article author
article_date    = page_soup.findAll("div", {"class": "time each_row"})          #select article date
article_tags    = page_soup.findAll("div", {"class": "topic_list"})             #select article tags

article_title_string    = article_title[0].h1.text                              #convert title into string
article_author_string   = article_author[0].text                                #converted author into string
article_date_string     = article_date[0].text                                  #converted date into string

article_tag_string          = article_tags[0].text                              #converted tags into string
article_tag_string          = article_tag_string.replace("\n", ", ")            #replaces new line[ \n ] with comma[ , ]
#print (article_body)
article_tag_string_length   = len(article_tag_string)                           #find the length of tag string
article_tag_string          = article_tag_string[2 : article_tag_string_length-2]   #select position 2 to last index of tag string
#print (article_tag_string)

tmp1 = "\n"     #for new line

filename        = "test.txt"
file_writer     = open(filename, "w", encoding="utf-8")
file_string     = ""
file_tag_string = ""


for div in article_body:
    article_paragraph = div.findAll("p")                #find all existing body paragraph
    for x in article_paragraph:
        file_string = file_string + x.text + "\n"       #concate all the paragraph into one string

#print(file_string)

'''file_writer.write("title, author, date, body\n" +
                  article_title_string + ", " +
                  article_author_string + ", " +            #csv formatted file writer
                  article_date_string + ", " +
                  file_string)'''

file_writer.write("Title    -   " + article_title_string    + tmp1 +
                  "Author   -   " + article_author_string   + tmp1 +
                  "Date     -  "  + article_date_string     + tmp1 +        #writes all the information in file
                  "Tags     -   " + article_tag_string      + tmp1 +
                  "Body     - \n" + file_string)
file_writer.close()


#print (div.find('a').contents[0])           ''' --------------------------------- '''
#print (div.find('img')['src'])              ''' |   some useful object elements | '''
#print (article_body[0].div.div.p)           ''' --------------------------------- '''
