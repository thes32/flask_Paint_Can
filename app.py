from flask import Flask, redirect, url_for, render_template
import datetime as dt
import requests
import databaseManager as sql

app=Flask(__name__)

@app.route("/")
def home():
    temp = getWeatherReport()
    return render_template("index.html",temp=temp, content="Paint")

@app.route("/<name>")
def user(name):
    return f"Hello, {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

def getWeatherReport():
    WEATHERAPI_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "0f09096e442eb490b11b317b45ba9e82"
    CITY = "Manchester"

    url = WEATHERAPI_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(url).json()

    temp = round(response['main']['temp'] - 273.15, 2)

    return temp

if __name__ == "__main__":
    sql.checkIfDBExists()
    app.run(debug=True)