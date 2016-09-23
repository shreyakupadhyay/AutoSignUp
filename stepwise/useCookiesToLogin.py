'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from Target website .
Description:
When we are getting data of a particular page of a website open that page in your browser, look for the network section
by using inspect element. And trace the request, get all the headers and according to the requirements of the 
website put the headers below. 
The most important thing here is that we can by pass the loing of any website by taking cookies and using them till they
gets expired.
'''
import logging
import requests
import re
import os
import sys
import time


logging.basicConfig(level=logging.DEBUG)
s = requests.Session()

headers = {
			":method":TYPE OF REQUEST (GET OR POST),
			":path":PATH TO THE PAGE,
			":scheme":THE PROTOCAL USED(HTTP,HTTPS),
			"accept":"application/json, text/plain, */*",
			"accept-language":ACCEPTING LANGUAGE,
			"content-type":DATA TYPE,
			"cookie": COOKIES FOR THAT PATICULAR PAGE,
			"origin":THE HOST OF THIS PATH,
			"referer":USR THE REFERER TO THIS PATH,
			"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
	}		

"""
Save data into appending a file of the type of output.
"""

def makeRequest():
	file = open(FILE TO SAVE OUTPUT,"a")
	response = s.post(link to the path of the website,headers=headers).text
	print (response)
	file.write(response)
	print (count)

makeRequest()