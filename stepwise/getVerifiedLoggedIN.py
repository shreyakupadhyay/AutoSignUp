'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : get verified for target website .
Description:
send a get request to get verified for the target website.
'''
import logging
import requests
import re
import os
import sys
import time
from bs4 import BeautifulSoup
import json

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()

def getVerified(LinkVerify):
	headers = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"accept-encoding":"gzip, deflate, sdch, br",
	"accept-language":"en-US,en;q=0.8",
	#"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
	}

	response = s.get(LinkVerify,headers=headers)
	responseText = response.text
	responseCookies = response.cookies
	print (responseCookies)

	"""
	The  line below is useful when there are some cookies which are there but you are able to get them using object.cookies.
	"""

	uid = requests.utils.dict_from_cookiejar(s.cookies)[key to the cookies]
	print (uid)

	dash_headers = {
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

	"""
	Put the link of the page to which you are getting directed after getting authenticated on the target website.
	And you are done. You logged in into the target website using a fake mail.
	"""

	response_dash = s.get(Link after verification,headers=dash_headers)
	print (response_dash.text)


getVerified(sys.argv[1])