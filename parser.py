#!/usr/bin/env python

import requests
import pprint
import os

os.system('cls' if os.name == 'nt' else 'clear')

def get_par():
	#q = raw_input('Where are you? ')
	#limit = int(input('Numer of tracks (1-10): '))
	query_params={
		#'q':q,
		'q':'Krakow',
		'units':'metric'}
	return query_params

def get_dat(ppp):
	endpoint = 'http://api.openweathermap.org/data/2.5/weather/'
	response = requests.get(endpoint, params=ppp)
	data = response.json()
	return data
	
def print_weather():
	os.system('cls' if os.name == 'nt' else 'clear')
	#pprint.pprint(data)
	print "Good morning %s!\n" %(data['name'])
	print data['weather'][0]['description'] + " today! :)"
	print "%i degrees out there." %(data['main']['temp'])
	
par = get_par()
data = get_dat(par)
print_weather()

