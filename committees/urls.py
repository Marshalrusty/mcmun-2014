from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Redirect committees/ back to committees (show the page)
    url(r'^$', 'cms.views.main', name='committees'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)', 'committees.views.view'),
)