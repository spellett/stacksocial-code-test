from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'stacksocial.views.index', name='index'),
    url(r'termSearch/$', 'stacksocial.views.term_tweets', name='term_page'),
    url(r'user/(?P<handle>[\w]+)/$', 'stacksocial.views.user_tweets', name='user_page'),
    # Examples:
    # url(r'^$', 'stacksocial.views.home', name='home'),
    # url(r'^stacksocial/', include('stacksocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
