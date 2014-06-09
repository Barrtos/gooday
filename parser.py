#!/usr/bin/env python

import requests
import pprint
import os

os.system('cls' if os.name == 'nt' else 'clear')

def get_par():
	q = raw_input('Where are you? ')
	#limit = int(input('Numer of tracks (1-10): '))
	query_params={
		'q':q,
		'units':'metric'}
	return query_params

def get_dat(ppp):
	endpoint = 'http://api.openweathermap.org/data/2.5/weather/'
	response = requests.get(endpoint, params=ppp)
	data = response.json()
	return data
	
def print_weather():
	os.system('cls' if os.name == 'nt' else 'clear')
	print "Weather for a good start!\n"
	pprint.pprint(data)
	print "Good morning %s!" %(data['name'])
	print data['main']['temp']
	
parameters=get_par()
data = get_dat(parameters)
print_weather()

