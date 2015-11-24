from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'baware.website.views.home', name='home'),
    url(r'^CrimeByLocation/', 'baware.website.views.Crime', name='Crime'),
)
