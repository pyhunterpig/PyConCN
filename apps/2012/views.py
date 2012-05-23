#coding=utf-8
from uliweb import expose

@expose('/2012/')
def index():
    return '<h1>Hello, Uliweb</h1>'
