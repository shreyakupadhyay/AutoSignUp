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
		"name":"shreyakupadhyay",
		"email":"shreyakupadhyay@gustr.com",
		"password":"1234567890"
	}

	response = s.post("https://gradbusters.com/signup",params=params,headers=headers)
	print (response.text)



getToken()

# def SignUp(Token,cookies):
# 	params = {
# 	"_token":Token,
# 	"name":"Thon1972",
# 	"email":"Thon1972@cuvox.de",
# 	"password":"1234567890"
# }
# 	response = s.post("https://gradbusters.com/signup",params=params,headers=headers)
# 	print (response.text)

#SignUp(getToken())

