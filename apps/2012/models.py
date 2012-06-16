#! /usr/bin/env python
#coding=utf-8
from uliweb.orm import *
from uliweb.utils.common import get_var

def get_modified_user():
    from uliweb import request
    
    return request.user.id

class Page(Model):#页面内容
    name = Field(str, verbose_name='页面名称', max_length=100)
    cncontent = Field(TEXT, verbose_name='中文内容')
    encontent = Field(TEXT, verbose_name='英文内容')
    created_on = Field(datetime.datetime, verbose_name='创建时间', auto_now_add=True)
    updated_on = Field(datetime.datetime, verbose_name='修改时间', auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.name
    
    class AddForm:
        fields = ['name', 'cncontent', 'encontent']
        
    class EditForm:
        fields = ['name', 'cncontent', 'encontent']


