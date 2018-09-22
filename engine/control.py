import re

# simple error 404 view without render
def error404(request):
    return ('404 Not Found',[('Content-Type','text/plain; charset=UTF-8')], '404 page not found')

# checks for slashes
def check_slash(i_str):
    if i_str[-1] == '/':
        return i_str[:-1]
    else:
        return i_str

# func for defining urls in url list
def url(pattern, view):
    return [pattern, view]

# func for parsing the url
def url_parse(method, path, url_list):
    for url in url_list:
        print(path)
        matches = re.search(url[0], path)
        if matches is not None:
            return url[1]           
    return error404    

# renders html
def render(html_file, variables_dict={}):
    html_file = open(html_file,'r')
    html_raw = html_file.read()
    html_file.close()
    match = re.search(r"\{\{(\w+)\}\}", html_raw)
    if match is not None:
        for match_ in match.groups():
            html_raw = re.sub(r"\{\{" + match_ + r"\}\}",
                              f"{variables_dict[match_]}", html_raw)
    return ('200 OK', [('Content-Type', 'text/html; charset=UTF-8')], html_raw)

# generic static_view
def static_view(request):
    ROUTE = request['PATH_INFO']
    ROUTE = check_slash(ROUTE)
    extension = ROUTE.split('.')[1]
    if extension in ("gif","jpeg","png","svg","bmp","webp"):
        content_type = f"image/{extension}"
    elif extension in ("css"):
        content_type = "text/css"
    elif extension in ("midi","mpeg","webm","ogg","wav"):
        content_type = f"audio/{extension}"
    elif extension in ("webm","ogg"):
        content_type = f"video/{extension}"
    elif extension == "js":
        content_type = "application/javascript"
    try:
        static_file = open(ROUTE[1::],'r')
        static_raw = static_file.read()
        static_file.close()
        return ('200 OK', [('Content-Type', f'{content_type}')], static_raw)
    except:
        return ('400 Bad Request',[], '404 Bad Request')