#! /usr/bin/env python
#coding=utf-8
from uliweb.core.dispatch import bind

@bind('prepare_view_env')
def prepare_template_env(sender, env, request):
    from views import menus
    env['menus'] = menus
