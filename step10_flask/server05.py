import random

from flask import Flask
from urllib.parse import urlencode
import requests
from urllib.request import urlopen, Request
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET



app = Flask(__name__)


# 태그 사용 가능

# '/' : 홈페이지
@app.route('/')
def hello_world():
    return '''
     <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    <li><a href="/read/1">HTML</a></li>
                    <li><a href="/read/2">CSS</a></li>
                    <li><a href="/read/3">JS</a></li>
                </ol>
                <h2>Welcome</h2>
                Hello, Web
            </body>
        </html>
    '''

@app.route('/create')
def create():
    return '<h2> Create </h2>'

@app.route('/read/<id>')
def read(id):
    return '<h2> Read %s </h2>' %id




# 디버깅 실행 형식
app.run(debug=True)