'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : signup into SECURED website .
Description:
Signup for the SECURED website to get a authentication mail.
'''
import logging
import requests
import re
import os
import sys
import time
from bs4 import BeautifulSoup




email = sys.argv[1]
[name, domain] = email.split('@')
# name ,domain ,email = sys.argv[1] , sys.argv[2] , sys.argv[3]   
print (name)
print (domain)
print (email)

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()


def sendPost():
	headers = {
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"en-US,en;q=0.8",
			"upgrade-insecure-requests":"1",
			"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
	}
	
	signUp_response = s.get(LINK TO SIGN UP PAGE,headers=headers)
	responseText = signUp_response.text

	regex = "USE REGEX TO FIND A PARAMETER REQUIRED FOR THE POST REQUEST FOR SIGN UP"
	result = re.findall(re.compile(regex),responseText)

	token = result[0]

	headers = {
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"en-US,en;q=0.8",
			"upgrade-insecure-requests":"1",
			"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
			"cookies":str(signUp_response.cookies),
			"origin":ORIGIN TO THE WEBSITE,
			"referer": REFERER TO THE REQUEST
	}

	params = {
		"_token":token,
		"name":name,
		"email":email,
		"password":password
	}
	
	response = s.post(SEND THE POST REQUEST CONTAINING ALL PARAMETERS,params=params,headers=headers)



sendPost()

"""
WAIT SO THAT CONFIRMATION MAIL IS SENT TO THE FAKE MAIL GENERATOR SERVER. HERE I AM USING fakemailgenerator.com WEBSITE.
"""

time.sleep(5)

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

"""
THIS FUNCTION RETURNS THE LINK TO THE CONFIRMATION MAIL AS HERE YOU WILL BE GETTING THE LINK TO ALL THE MAILS IN YOUR INBOX AND
MOST PROBABLY THE FIRST ONE CONTAINS THE CONFIRMATION MAIL.
"""

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

"""
THIS FUNCTION RETURNS THE LINK OF THE VERIFICATION.
"""

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
	return authLink
	
	

domain = domain.replace('@','')
verificationLink = getMailLink(name,domain)

"""
THIS FUNCTION FINALLY ALLOWS TO GET VERIFIED AND LOGIN INTO THE WEBSITE YOU WANT USING THE SCRIPT AND WITH A FAKE MAIL.
"""

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()

def getVerified(LinkVerify):
	headers = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"accept-encoding":"gzip, deflate, sdch, br",
	"accept-language":"en-US,en;q=0.8",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
	}

	response = s.get(LinkVerify,headers=headers)
	responseText = response.text
	responseCookies = response.cookies
	print (responseCookies)
	print (responseCookies["XSRF-TOKEN"])

	headers = {
			"cache-control":"max-age=0, no-cache",
			"cache-control":"no-cache",
			"cf-ray":"2e5c0ada1b242dc7-BOM",
			"content-encoding":"gzip",
			"content-type":"text/html; charset=UTF-8",
			"date":"Wed, 21 Sep 2016 08:10:45 GMT",
			"server":"cloudflare-nginx",
			"set-cookie": str(responseCookies),
			"status":"200",
			"vary":"Accept-Encoding",
			"x-mod-pagespeed":"1.11.33.2-0",
			"x-powered-by":"PHP/5.6.24"
	}

	response = s.get(LINK TO THE GET REQUEST WHICH OCCURS AFTER GIVING THE VERIFICATION LINK,headers=headers)
	print (response.text)

getVerified(verificationLink)