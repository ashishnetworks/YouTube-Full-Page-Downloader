#!/usr/bin/python
# -*- coding: utf-8 -*-

#Developed by @ashish_net twitter handle

import requests
from bs4 import BeautifulSoup
import sys,os,subprocess

def googlesearch(searchfor):
    link = 'https://www.youtube.com/results?'
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
    payload = {'search_query': searchfor}
    response = requests.get(link, headers=ua, params=payload)

    with open('youtube_output.html', 'w') as file_:
        file_.write(response.text.encode('utf8'))

    soup=BeautifulSoup(response.content,'html5lib')
    try:
        section=soup.find('ol',class_='item-section')
        with open('section.html', 'w') as file_:
            file_.write(section.encode('utf8'))

        vidios=section.find_all('h3')

    except IndexError:
        print "results could not be founds"

    i=1
    for vidio in vidios:

        try:
            print "Downloading vidio num: %s "%i
            print "Vidio Name :"+vidio.find('a',href=True).string
            link = "http://youtube.com%s" % vidio.find('a',href=True)['href']
            command="youtube-dl -citk %s"%link
            subprocess.call(command, shell=True)

        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message

        i=i+1

googlesearch(sys.argv[1])


