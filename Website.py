from bottle import route, run, template, view, static_file, request, redirect, error
import requests
from datetime import datetime
@route('/')
def index():
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   return template('index', time=current_time)
run(host='0.0.0.0', port=4000, reloader=True, debug=True)