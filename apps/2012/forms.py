#coding=utf-8
from uliweb.form import *


class EditorForm(Form):
    form_buttons = Submit(value="保存", _class="btn")
    form_title = "编辑"
    
    name = StringField(label="页面名称", required=True)
    cncontent = TextField(label="中文内容", required=True)
    encontent = TextField(label="英文内容")

    
    
    
