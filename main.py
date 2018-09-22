import waitress
from engine.wsgi import wsgi_app

def aplicacao(env, init_response):
    (status, headers, content)= wsgi_app(env)
    print(status)
    init_response(status, headers)
    yield content.encode('utf-8')

waitress.serve(aplicacao)