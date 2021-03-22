import requests



# Making request to server for data 
def makeRequest(cityname , countrycode):
	re = requests.get("http://api.openweathermap.org/data/2.5/weather",params={ "q":{cityname,countrycode} ,"appid":KEY})
	return re.json()



# get the temperature in celsius
def  temp(cityname, countrycode):
	data = makeRequest(cityname, countrycode)
	data = data['main']['temp']
	temp_cel = float(data)-273.15  # converting kelvin to celsius
	return f"{round(temp_cel,2)}"

	

# get humidity in %
def  humid(cityname , countrycode):
	data = makeRequest(cityname ,  countrycode)
	humidity = int(data['main']['humidity'])
	return f"{humidity} %"




# get weather
def  weather(cityname , countrycode):
	data = makeRequest(cityname , countrycode)
	weath = data['weather'][0]['main']
	return weath 











