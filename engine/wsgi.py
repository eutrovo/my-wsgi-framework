from engine.control import url_parse
from urls import url_list

def wsgi_app(env):
    method = env['REQUEST_METHOD']
    path = env['PATH_INFO']
    view_result = url_parse(method, path, url_list)(env)
    return view_result