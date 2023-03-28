from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# WeatherStack API key
API_KEY = '4f4debf1e04e3ebb36b9944c8fc066ec'

# Route for displaying the weather form
@app.route('/')
def weather_form():
    return render_template('index.html')

# Route for processing the weather form
@app.route('/', methods=['POST'])
def weather():
    # Get the user's city input from the form
    city = request.form['city']

    # Call the WeatherStack API to get the current weather for the city
    response = requests.get(f'http://api.weatherstack.com/current?access_key={API_KEY}&query={city}')
    data = response.json()

    # Extract the relevant weather information from the API response
    temperature = data['current']['temperature']
    description = data['current']['weather_descriptions'][0]

    # Return the weather information to the user
    return render_template('weather.html', city=city, temperature=temperature, description=description)

if __name__ == '__main__':
    app.run()

