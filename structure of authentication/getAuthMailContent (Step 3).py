'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting emails content from the fake mail server.
Description:
Using a fake mail server and getting email content from the fake mail server to get the link to confirmation email of the target website.
'''
import logging
import requests
import re
import os
import sys
import time
from bs4 import BeautifulSoup

headers = {
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate, sdch",
			"Accept-Language":"en-US,en;q=0.8",
			"Connection":"keep-alive",
			"Cookie":"__cfduid=ddd0529779bfee54060fedec5750e47f01474318694; _gat=1; _ga=GA1.2.1971555940.1474318696; __atuvc=3%7C38; __atuvs=57e05167d2fb7690002",
			"Host":"www.fakemailgenerator.com",
			"Upgrade-Insecure-Requests":"1",
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()

def getMailLink(id_head,id_domain):
	response = s.get("http://www.fakemailgenerator.com/inbox/"+id_domain+"/"+id_head,headers=headers)
	responseText = response.text
	soup = BeautifulSoup(responseText,'lxml')
	for link in soup.findAll('a'):
		if link.has_attr('href'):
			if("/inbox/" in link["href"]):
				print link["href"]
				emailLink = link["href"].replace("/inbox/","/email/")
				print emailLink
				getMailContent(emailLink)


def getMailContent(link):
	emailResponse = s.get("http://www.fakemailgenerator.com"+link,headers=headers)
	emailResponseText = emailResponse.text
	soup = BeautifulSoup(emailResponseText,'lxml')
	for link in soup.findAll('a', href=True, text={'Confirm Email'}):
		authLink = link["href"]
	print authLink


email = sys.argv[1]
[name, domain] = email.split('@')
print (name)
print (domain)
print (email)

getMailLink(name,domain)
