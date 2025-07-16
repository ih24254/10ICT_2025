from bottle import route, run, template, view, static_file, request, redirect, error
import requests
from datetime import datetime
@route('/')
def index():
    name = 'Isaiah'
    response = requests.get(f"https://api.agify.io/?name={name}")
    response = response.json()
    age = response['age']
    return template('index', name=name, age=age)
run(host='0.0.0.0', port=4000, reloader=True, debug=True)