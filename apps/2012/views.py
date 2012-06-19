#coding=utf-8
from uliweb import application, expose, response, settings, decorators
from uliweb.i18n import ugettext_lazy as _ , get_language
from models import Page


menus = settings.MENUS.MENUS or [
    ('about', _('关于大会'), '/2012/about'),
    ('schedule', _('日程安排'), '/2012/schedule'),
    ('venue', _('会场交通'), '/2012/venue'),
    ('registration', _('报名注册'), '/2012/registration'),
    ('volunteer', _('志愿者'), '/2012/volunteer'),
    ('sponsors', _('赞助商'), '/2012/sponsors'), 
    ('Weibo', _('官方微博'), 'http://weibo.com/pyconcn'),
]

@expose('/2012/')
def index2012():
    msg = []
    pagecontent = ''
    return dict(pageTitle="PyCon China 2012", 
                msg=msg,
                pagecontent=pagecontent)

@decorators.require_login
@expose('/2012/editor/<path:urlpath>')
def editor(urlpath):
    """页面编辑"""
    pagename = urlpath.split("/")[0]
    from forms import EditorForm
    from uliweb.orm import get_model
    Page = get_model('page')
        
    if request.method == 'GET':
        page = Page.get(Page.c.name==pagename)
        if page:
            form = EditorForm({'name': page.name,
                               'cncontent': page.cncontent,
                               'encontent': page.encontent}
                             )
            
        else:
            form = EditorForm({'name':pagename})
        return {'form':form, 'msg':''}
    if request.method == 'POST':
        name = request.params.get('name','')
        cncontent = request.params.get('cncontent','')
        encontent = request.params.get('encontent','')
        page = Page.get(Page.c.name==name)
        if page:
            page.cncontent = cncontent
            page.encontent = encontent
            page.save()
        else:
            page = Page(name=name,cncontent=cncontent,encontent=encontent)
            page.save()
        
    return redirect('/2012/%s' %name) 
    



@expose('/2012/<path:urlpath>')
def lookup(urlpath):
    filename = "2012/%s.html" %urlpath.split("/")[0]
    if not application.get_file(filename, dir='templates'):
        filename = '2012/default.html'
    response.template = filename
    msg = []
    page = Page().get(Page.c.name==urlpath.split("/")[0])
    if page:
        if get_language() == 'zh_CN':
            pagecontent = page.cncontent
        else:
            pagecontent = page.encontent
    else:
        pagecontent = ''
    return dict(pageTitle="%s -- PyCon China 2012" %urlpath.split("/")[0],
                msg=msg,
                pagecontent=pagecontent)