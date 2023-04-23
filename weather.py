from flask import Flask, render_template, request, abort, Response
import urllib
import json


# initialize the Flask application
app = Flask(__name__)

# extrace the city name; retrieve the wather for requested city from 'OpenWeatherMap'; shows weather page
@app.route('/forecast', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if city is None:
        print("[error]")
        abort(400, 'Missing argument city')

    data = {}
    data['q'] = request.args.get('city')    # name of the city for witch we want forecast
    data['appid'] = '1fe7cb09e4cdef347e66d09abb5a4b9f'    # is your 'OpenWeatherMap' API Key
    data['units'] = 'metric'
    print("[data]: ", data)

    url_values = urllib.parse.urlencode(data)    # reading, editing and creating URLs
    print("[url_values]: ", url_values)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    print("[full_url]: ", full_url)
    data = urllib.request.urlopen(full_url)    # access t resource on the Internet
    print('[data]: ', data)

    resp = Response(data)    # return the status code from web page
    print("[resp]: ", resp)
    print("[resp.status_code]: ", resp.status_code)
    resp.status_code = 200    # MAKES NO SENSE
    return render_template('index.html', title='Weather App', data=json.loads(data.read().decode('utf8')))

if __name__ == "__main__":
    print("main")
    app.run(port=5000, debug=False, threaded=True)