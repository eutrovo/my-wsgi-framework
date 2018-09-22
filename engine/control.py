import re

def check_slash(i_str):
    if i_str[-1] == '/':
        return i_str[:-1]
    else:
        return i_str

def url(pattern, view):
    return [pattern, view]

def url_parse(method, path, url_list):
    for url in url_list:
        matches = re.search(url[0], path)
        if matches is not None:
            return url[1]
    

def render(html_file, variables_dict={}):
    html_file = open(html_file,'r')
    html_raw = html_file.read()
    html_file.close()
    match = re.search(r"\{\{(\w+)\}\}", html_raw)
    if match is not None:
        for match_ in match.groups():
            html_raw = re.sub(r"\{\{" + match_ + r"\}\}",
                              f"{variables_dict[match_]}", html_raw)
    return ('200 OK', [('Content-Type', 'text/plain; charset=UTF-8')], html_raw)