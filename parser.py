#!/usr/bin/env python

import requests
import pprint
import os

os.system('cls' if os.name == 'nt' else 'clear')

def get_par():

	print 'Weather for a good start!\n'
	#user = raw_input('User name (ex. Msitake): ')
	#limit = int(input('Numer of tracks (1-10): '))
	query_params={
		'q':'Krakow',
		'units':'metric'}
	return query_params, limit, user

def get_dat(ppp):
	endpoint = 'http://api.openweathermap.org/data/2.5/weather/'
	response = requests.get(endpoint, params=ppp)
	data = response.json()
	return data
	
parameters, li, user= get_par()
data = get_dat(parameters)

os.system('cls' if os.name == 'nt' else 'clear')
print "Best %s tracks for user %s overall! \n" %(li, user)
track = []
#pprint.pprint(data)

	
with open("results.html", "w") as textfile:
	textfile.write("<!DOCTYPE html><html><head><link type=\"text/css\" rel=\"stylesheet\" href=\"stylesheet.css\"/><title>LFM Track Grab</title></head><body><div><img src=\"http://www.justinparks.com/wp-content/uploads/2009/10/lastfm-logo-square-webtreatsetc.png\"/><p><h2>Last.fm top ")
	textfile.write(str(li)) 
	textfile.write(" tracks from user: ")
	textfile.write(str(user)) 
	textfile.write("!</h2></p>")
	
	textfile.write("<br/><br/></div></body></html>")

