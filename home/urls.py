from django.conf.urls import patterns, include, url

from home.views import Home


urlpatterns = patterns('home.views',
    # Examples:
    # url(r'^$', 'cowhite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='homepage'),
)
