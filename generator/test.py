# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('test.html')
template.stream(foo='Hello World!').dump('../test.html')

