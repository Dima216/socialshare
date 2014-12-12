from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'heroku_project.views.home', name='home'),
    url(r'^', include('heroku_app.urls')),
)
