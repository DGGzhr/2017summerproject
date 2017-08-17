#!/bin/env/python
import dns.resolver
import requests
import json
import urllib2
import re
import time
import os
import threading
import timeit
import geoip2.database
import signal
import MySQLdb
import sys

#w=open('7-14-error','w')

def   whois(domain):
  try:
    
    domain=domain.rstrip('.')
    command='whois '+domain
    c=os.popen(command)
    string=c.read()
    created = 'Creation\sDate\:\s\d\d\-\w{3}\-\d{4}'
    Updated='Updated\sDate\:\s\d\d\-\w{3}\-\d{4}'
    created1 = 'Creation\sDate\:\s\d{4}\-\d\d\-\d\d'
    Updated1='Updated\sDate\:\sd{4}\-\d\d\-\d\d'
    registrationed='Registration\sTime\:\s\d{4}\-\d\d\-\d\d'
    match1 = (re.findall(created,string))
    match4=(re.findall(registrationed,string))
    match3=(re.findall(created1,string))
    #print match3
    if match1!=[]:
        #print '1'
        creat=time.mktime(time.strptime(match1[0][-11:],"%d-%b-%Y"))
      
       
        now=time.time()
        year1=(now-creat)/31536000
        return year1
    elif match4!=[]:
        registration=time.mktime(time.strptime(match4[0][-10:],"%Y-%m-%d"))
        now=time.time()
        year1=(now-registration)/31536000
        return year1
    elif match3!=[]:
	creat=time.mktime(time.strptime(match3[0][-10:],"%Y-%m-%d"))
        now=time.time()
        year1=(now-creat)/31536000
        return year1
    else:
	return 'null'

  except:
  	
	return 'null'


def  qname(s):
	thread=[]
	ip=[]
	info=[]
	country=[]
	info.append(s)
	domain = s
	len_A = 0
	NS_count=0
	ttl=0
	len_AR=0
	try:
		A = dns.resolver.query(domain,'A')
		for i in A.response.answer:

			len_A=len(i)
			info.append(len_A)
			info.append(i.ttl)
			try:
				for j in i.items:
					ip.append(j.address)
			except:

				print '62error'
				#.write(domain)
	except:
	 	info.append(0)
		info.append(0)
		#w.write(domain)
	try:
		NS= dns.resolver.query(domain,'NS')
		for i in NS.response.answer:
			info.append(len(i))
			info.append(i.ttl)

		if len(i)>1:
			for j in i.items:
				try:
					A= dns.resolver.query(j.to_text(), 'A')
					for k in A.response.answer:
						ttl=ttl+k.ttl
						len_AR=len_AR+1
					for j in k.items:
						ip.append(j.address)
				except:
					info.append(0)
					info.append(0)
	except:
		for i in range(2):
			info.append(0)
	for i in ip:
		try:
			coun=checkip(i)
			if coun!=0 and coun!=None:
				country.append(coun)
		except:
			print '104error'

	country = list(set(country))
	info.append(len_AR)
	if len_AR!=0:
		info.append(ttl/len_AR)
	else:
		info.append(0)
	info.append(len(country))
	info_whois= whois(domain)
	#print info_whois
	if info_whois!='null':
		info.append(info_whois)
	else: 
		info.append(0)
	return info
def checkip(ip):
    try:
	reader = geoip2.database.Reader('/home/spark/geo/GeoLite2-Country.mmdb')
        response = reader.country(ip)
	return response.country.name
    except:
	print 'check error'
def weizhi(ip):
	reader = geoip2.database.Reader('/home/spark/geo/GeoLite2-City.mmdb')
	response = reader.city(ip)
	return r


#print qname(sys.argv[1])
