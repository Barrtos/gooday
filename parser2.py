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
	print "Good morning %s! :)\n" %(data['name'])
	print data['weather'][0]['description'] + " today!"
	print "%i degrees outdoors." %(data['main']['temp'])
	
par = get_par()
data = get_dat(par)
print_weather()


with open("results.php", "w") as textfile:

#Html init
	textfile.write("<html><head><link type=\"text/css\" rel=\"stylesheet\" href=\"stylesheet.css\"/><title>GooD'ay</title></head><body>")
	
#Image	
	#textfile.write("<div><img src=\"http://www.justinparks.com/wp-content/uploads/2009/10/lastfm-logo-square-webtreatsetc.png\"/><p><h2>Last.fm top ")
	
#Grooveshark widget
	#textfile.write('<object width="250" height="250" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" id="gsPlaylist9858105448" name="gsPlaylist9858105448"><param name="movie" value="http://grooveshark.com/widget.swf" /><param name="wmode" value="window" /><param name="allowScriptAccess" value="always" /><param name="flashvars" value="hostname=grooveshark.com&playlistID=98581054&p=1&bbg=000000&bth=000000&pfg=000000&lfg=000000&bt=FFFFFF&pbg=FFFFFF&pfgh=FFFFFF&si=FFFFFF&lbg=FFFFFF&lfgh=FFFFFF&sb=FFFFFF&bfg=666666&pbgh=666666&lbgh=666666&sbh=666666" /><object type="application/x-shockwave-flash" data="http://grooveshark.com/widget.swf" width="250" height="250"><param name="wmode" value="window" /><param name="allowScriptAccess" value="always" /><param name="flashvars" value="hostname=grooveshark.com&playlistID=98581054&p=1&bbg=000000&bth=000000&pfg=000000&lfg=000000&bt=FFFFFF&pbg=FFFFFF&pfgh=FFFFFF&si=FFFFFF&lbg=FFFFFF&lfgh=FFFFFF&sb=FFFFFF&bfg=666666&pbgh=666666&lbgh=666666&sbh=666666" /><span><a href="http://grooveshark.com/search/playlist?q=z.morning%20Kestrel" title="z.morning by Kestrel on Grooveshark">z.morning by Kestrel on Grooveshark</a></span></object></object>')
	
#City input form
	textfile.write('<form>Personalize your good day! :)<p>Where are you: <input type="text" name="city"><br><input type="submit" value="GooD\'ay!"></form>')
	textfile.write("<?php $f = fopen(\"user_data.txt\", \"w\");fwrite($f, $_POST[\"city\"]); fclose($f);$f = fopen(\"user_data.txt\", "r");echo fgets($f); fclose($f);?>")
	textfile.write("</p>")
	textfile.write("<br/><br/></div></body></html>")
