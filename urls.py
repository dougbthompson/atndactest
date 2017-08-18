
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = ('', 
    # url(r'^$',views.index, name="index"),
    url(r'^atn1/',  include('atn1.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls)
)

