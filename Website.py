from bottle import route, run, template, view, static_file, request, redirect, error
import requests
from datetime import datetime


@route('/')
@route('/home')
@view('homepage')
def index():
     pass

#main routine
run(host='0.0.0.0', port=4000, reloader=True, debug=True)