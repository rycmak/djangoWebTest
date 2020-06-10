from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #url(r'^video/(?P<vid>\w+)/$',views.display_video),
    # \w will allow alphanumeric characters or string
    path('', views.index, name="index"),
    #path('', views.display_video, name="video_template"),
]