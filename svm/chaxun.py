import svm
import sys
import qname
import os
import re
from  tld import get_tld
import dns.resolver
import geoip2.database
import string
import MySQLdb

key={}
def weizhi(ip):
    try:
        reader = geoip2.database.Reader('/home/ubuntu/geo/GeoLite2-City.mmdb')
        response = reader.city(ip)
        return response.country.name.encode('ascii',errors='ignore'),response.city.name.encode('ascii',errors='ignore'),response.location.latitude,response.location.longitude
    except:
	return 'None','None','None','None'
def whois(domain):
	command='whois '+domain
    	c=os.popen(command)
    	string=c.read()
	created = 'Creation\sDate\:\s\d\d\-\w{3}\-\d{4}'
	created1 = 'Creation\sDate\:\s\d{4}\-\d\d\-\d\d'
	registrationed='Registration\sTime\:\s\d{4}\-\d\d\-\d\d'
	match1 = (re.findall(created,string))
    	match4=(re.findall(registrationed,string))
	match2=(re.findall(created1,string))
	if match1!=[]:
		return match1[0][15:]
	elif match4!=[]:
		return match4[0][19:]
	elif match2!=[]:
		return match2[0][15:]
	else:
		return 'null'
def ip(domain):
	ip=[]
	try:
		A = dns.resolver.query(domain,'A')
		for i in A.response.answer:
			for j in i.items:
				ip.append(j.address)
		try:
			NS= dns.resolver.query(domain,'NS')
			for i in NS.response.answer:
				if len(i)>1:
                       			for j in i.items:
						try:
							A= dns.resolver.query(j.to_text(), 'A')
							for k in A.response.answer:
								for j in k.items:
	
									ip.append(j.address)
						except:
							continue
		except:
			print '43error'
	except:
		print '45error'
	if len(ip)<4:
		for i in range(4-len(ip)):
			ip.append('null')
		return ip
	else:
		return ip[:4]



if __name__=="__main__":
	domain=sys.argv[1]
	db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306,db='malicious_domain')
	list=""
	lo="None,None,None,None,"
	result=0
	domain=get_tld("htpp://"+domain.strip('.').strip('\n'))
	feature=qname.qname(domain)
	
	for i in svm.get_feature(domain):
		feature.append(i)
	#print feature
	cursor=db.cursor()
	sql="select domain from domain where domain = '%s'"%(domain)
	cursor.execute(sql)
	length=len(cursor.fetchall())
	if length==0 and len(feature)==22 and feature[8]!='0':	
		result=svm.predict_domain(feature)[0]
	elif length>0:
		result=-1
	elif len(feature)!=22:
		result=0
	time=whois(domain)
	ip=ip(domain)
	for i in ip[0:3]:
		list=(list+str(i)+',') 
	list=list+ip[3]
	for i in ip:
		location=weizhi(i)
		if  location != ('None','None','None','None'):
			lo = ""	
			for i in location:
				lo=lo+str(i)+','
			break;
		
	s=domain+','+str(result)+','+str(time)+','+lo+list
	print  s
	#print weizhi(116.251.205.124)
