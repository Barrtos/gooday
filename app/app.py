# -*- coding: utf-8 -*-
import web
import requests
import pprint
import os


#Weather API

def get_par(city):
	query_params={'q':city,'units':'metric'}
	return query_params

def get_dat(ppp):
	endpoint = 'http://api.openweathermap.org/data/2.5/weather/'
	response = requests.get(endpoint, params=ppp)
	data = response.json()
	return data

urls = (
  '/hello', 'Index'
)



#Rendering Index page

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout") #layout wrap around

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "GooD'ay! Good morning %s, good morning %s!" %(form.name, form.city)
        temperature = "%s °C" %(get_dat(get_par(form.city))['main']['temp'])
        desc = "%s today" %(get_dat(get_par(form.city))['weather'][0]['description'])
        return render.index(greeting = greeting, temperature = temperature, desc = desc)

if __name__ == "__main__":
    app.run()
    
    

