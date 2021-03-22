from flask import Flask, render_template, request
from webrequest import makeRequest, temp, humid, weather


app = Flask(__name__)



@app.route("/")
def hello():
	return render_template("index.html")



@app.route("/submit", methods=["POST"])
def submit():
	city_name = request.form.get("cityname")
	country_code = request.form.get("countrycode")
	temp_txt = temp(city_name, country_code) # Store temperature of city
	humid_txt = humid(city_name, country_code) # Store humidity of ciy
	weather_txt = weather(city_name, country_code) # Store weather of city

	return render_template("layout.html",temp_txt=temp_txt,city_name=city_name ,humid_txt=humid_txt,weather_txt=weather_txt)


if __name__ == "__main__":
	app.run(debug=True)