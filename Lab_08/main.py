from flask import Flask,render_template
import requests # type: ignore

app = Flask(__name__)

NASA_API_KEY = "this is my api key"
#Endpoints
apod_url = "https://api.nasa.gov/planetary/apod"

@app.route("/",methods=["GET"])
def index():
    #Fetching Data From NASA
    params = {"api_key":NASA_API_KEY}
    response = requests.get(apod_url,params=params)
    apod_data = response.json()
    return render_template("index.html",apod = apod_data)

if __name__ == "__main__":
    app.run(debug=False)
