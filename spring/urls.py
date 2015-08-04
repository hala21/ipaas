from django.conf.urls import patterns, url
from views import *

#admin.autodiscover()

urlpatterns = patterns('spring.views',
    # Examples:
    # url(r'^$', 'easyshow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),    
    
    url(r'^$', index,name="index"), 
)