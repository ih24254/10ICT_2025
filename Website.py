from bottle import route, run, template, view, static_file, request, redirect, error
import requests
from datetime import datetime

@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='./static')

@route('/')
@route('/home')
@view('homepage')
def index():
  pass

@route('/page1')
@view('/page1')
def sport_page():
  pass

  #main routine
run(host='0.0.0.0', port=4000, reloader=True, debug=True)