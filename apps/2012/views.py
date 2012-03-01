#coding=utf-8
from __future__ import with_statement
from uliweb import expose
from uliweb.orm import get_model
from uliweb import request

@expose('/2012/')
def index():
    return {} #'<h1>Hello, Uliweb</h1>'

@expose('/2012')
class siteView(object):
        
    def about(self):
        return dict(page=dict(pagename='about',cndata='')) 
    
    def schedule(self):
        return dict(page=dict(pagename='schedule',cndata=''))
    
    def venue(self):
        return dict(page=dict(pagename='venue',cndata=''))    

    def registration(self):
        return dict(page=dict(pagename='registration',cndata=''))
        
    def sponsors(self):
        return dict(page=dict(pagename='sponsors',cndata=''))

    def volunteer(self):
        return dict(page=dict(pagename='volunteer',cndata=''))
