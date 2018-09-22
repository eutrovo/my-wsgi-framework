from engine.control import url_parse
from urls import url_list

def wsgi_app(env):
    method = env['REQUEST_METHOD']
    path = env['PATH_INFO']
    view = url_parse(method, path, url_list)
    return view