'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : signup into gradbuster website .
Description:
Signup for the gradbuster website to get a authentication mail.
'''
import logging
import requests
import re
import os
import sys
import time
from bs4 import BeautifulSoup



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
	return id_head[0].get("value") , id_domain[0].getText() ,emailID

name ,domain ,email = getID() 
print (name)
print (domain)
print (email)

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()


def getToken():
	headers = {
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"en-US,en;q=0.8",
			"upgrade-insecure-requests":"1",
			"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
	}
	
	response = s.get("https://gradbusters.com/signup",headers=headers)
	responseText = response.text
	print (responseText)
	print (response.cookies)
	cookies = response.cookies
	regex = re.escape('<input type="hidden" name="_token" value="')+'(.+?)'+re.escape('">')
	result = re.findall(re.compile(regex),responseText)
	print (result[0])

	token = result[0]
	headers = {
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"en-US,en;q=0.8",
			"upgrade-insecure-requests":"1",
			"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
			"cookies":str(cookies),
			"origin":"https://gradbusters.com",
			"referer":"https://gradbusters.com/signup"
	}

	params = {
		"_token":token,
		"name":name,
		"email":email,
		"password":"1234567890"
	}
	print (name)
	print (domain)
	print (email)
	response = s.post("https://gradbusters.com/signup",params=params,headers=headers)
	print (response.text)



getToken()

time.sleep(10)

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


def getMailLink(id_head,id_domain):
	response = requests.get("http://www.fakemailgenerator.com/inbox/"+id_domain+"/"+id_head,headers=headers)
	responseText = response.text
	soup = BeautifulSoup(responseText,'lxml')
	for link in soup.findAll('a'):
		if link.has_attr('href'):
			if("/inbox/" in link["href"]):
				print (link["href"])
				emailLink = link["href"].replace("/inbox/","/email/")
				getMailContent(emailLink)


def getMailContent(link):
	emailResponse = requests.get("http://www.fakemailgenerator.com"+link,headers=headers)
	emailResponseText = emailResponse.text
	#regex = re.escape('<head/><div dir="ltr">')+'(.+?)'+re.escape('</div>')
	#result  = re.findall(re.compile(regex),emailResponseText)
	soup = BeautifulSoup(emailResponseText,'lxml')
	for link in soup.findAll('a', href=True, text={'Confirm Email'}):
		authLink = link["href"]
	#emailResponse = s.get(authLink)
	print (authLink)
	
	

domain = domain.replace('@','')
getMailLink(name,domain)