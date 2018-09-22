from app import views
from engine.control import url
from engine.control import static_view
# new
url_list = [
    url(r"^/$", views.index),
    url(r"^/static/(\w+)/", static_view),
]