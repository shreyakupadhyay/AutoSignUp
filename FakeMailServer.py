'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting emails from a fake mail server .
Description:
Using a fake mail server and getting emails from that which we are using on a particular website to get authenticated 
and taking cookies for that to login into the website.
'''
import logging
import requests
import re
import os
import sys
import time
from bs4 import BeautifulSoup



# logging.basicConfig(level=logging.DEBUG)
# s = requests.Session()
		



def getID():
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
	response = requests.get("http://www.fakemailgenerator.com",headers=headers)
	responseText = response.text
	soup = BeautifulSoup(responseText,'lxml')
	id_head = soup.findAll('input',attrs={'id':'home-email'}) # getting head name of the email ID
	id_domain = soup.findAll('span',attrs={'id':'domain'})   # getting domai of the email ID
	emailID = id_head[0].get("value") + id_domain[0].getText()
	print (emailID)
	return id_head[0].get("value")

val = getID() 


# def getMail(id_head):
# 	reponseMail = s.get("http://www.fakemailgenerator.com/inbox/armyspy.com/"+id_head,headers=headers)
# 	print reponseMail.text

# time.sleep(30)
# getMail(val)