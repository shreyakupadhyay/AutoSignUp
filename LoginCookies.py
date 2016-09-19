'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from gradbuster website .
Description:
Getting data from gradbuster website which uses login to get its data. And bypassing that using cookies. 
'''
import logging
import requests
import re
import os
import sys
import time

headers = {	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}

logging.basicConfig(level=logging.DEBUG)
s = requests.Session()
headers = {
			":authority":"gradbusters.com",
":method":"POST",
":path":"/dashboard/filter",
":scheme":"https",
"accept":"application/json, text/plain, */*",
"accept-encoding":"gzip, deflate, br",
"accept-language":"en-US,en;q=0.8",
"content-length":"13",
"content-type":"application/json;charset=UTF-8",
"cookie":"__cfduid=de0aba16c03d1a671ad0fd6f97864511a1474291171; _ga=GA1.2.623201218.1474291184; XSRF-TOKEN=eyJpdiI6IkZwVUZhK3FHdDFIa2JoYnd5aXAzYXc9PSIsInZhbHVlIjoiSTc3dTE2QVlkWlBpU2ZkdVwvbGh5QzhGcTA3aE9ST2ZXUXBIQVlpcHRXOVJxd1hJSkJWOXR3TlA2S0JSdUtUVHlJNXFYc3I0dFVvTmlobFhtVEZVWlJnPT0iLCJtYWMiOiIyZmRmZGE5MTc5YzM5OTdjNWMwMGVjZDg3MWRiZWJjMGYwZjIzNGQ3OWRkMjA1NDY2OTQ5YjRhOWUxMjU2OTEzIn0%3D; laravel_session=eyJpdiI6Imo1RTdvQXREcmNaSXFlVnZOYytneVE9PSIsInZhbHVlIjoiN091RnE2MVgreUtTTHBLU1pFcVQ4N1NPTWNuck5lbTduTlRhTDVCekFoZ0NWZWpaMGI5Yit2aE4rNnBoeEpJb1UwXC9ydDlOTWhPd2lzTjl0VnRWb1pRPT0iLCJtYWMiOiIyNzdjMjY5NzE2ZGUxNWExZDI0YTQyM2I1ODljZDZjNmFjNTc2NTQyNjEwY2NmM2JkMjMyOWYwMGY1NWUzYWE4In0%3D",
"origin":"https://gradbusters.com",
"referer":"https://gradbusters.com/dashboard/table",
"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
"x-xsrf-token":"eyJpdiI6IkZwVUZhK3FHdDFIa2JoYnd5aXAzYXc9PSIsInZhbHVlIjoiSTc3dTE2QVlkWlBpU2ZkdVwvbGh5QzhGcTA3aE9ST2ZXUXBIQVlpcHRXOVJxd1hJSkJWOXR3TlA2S0JSdUtUVHlJNXFYc3I0dFVvTmlobFhtVEZVWlJnPT0iLCJtYWMiOiIyZmRmZGE5MTc5YzM5OTdjNWMwMGVjZDg3MWRiZWJjMGYwZjIzNGQ3OWRkMjA1NDY2OTQ5YjRhOWUxMjU2OTEzIn0=",
}		
count = 0
file = open("data7.json","a")
for i in range(542,700):	
	response = s.post("https://gradbusters.com/dashboard/filter?page="+str(i),headers=headers).text
	print (response)
	file.write(response)
	print (count)
	count = count + 1
	time.sleep(15)
