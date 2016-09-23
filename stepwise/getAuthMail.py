'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : signup into target website .
Description:
Signup for the target website to get a authentication mail.
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


