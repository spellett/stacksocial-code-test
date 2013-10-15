from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('stacksocial.views',
    url(r'^$', 'index', name='index'),
    url(r'termSearch/$', 'term_tweets', name='term_page'),
    url(r'user/(?P<handle>[\w]+)/$', 'user_tweets', name='user_page'),
    url(r'test/$', 'test_form', name='test_form'),
    #url(r'uploadDocument/$', 'upload_doc', name='upload_doc_page'),
    # Examples:
    # url(r'^$', 'stacksocial.views.home', name='home'),
    # url(r'^stacksocial/', include('stacksocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
