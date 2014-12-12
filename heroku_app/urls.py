from django.conf.urls import patterns, url


urlpatterns = patterns('',
	url(r'^$','heroku_app.views.home', name='home'),
	url(r'^(?P<ref_id>.+)/$','heroku_app.views.share', name='share'),
	) 